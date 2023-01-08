from flask import render_template, request, flash, redirect, session, url_for
from . import bp_acc
from ServeIT.auth.auth import login_required
from ServeIT.models.dbUtils.UserRepo import UserRepo
from .forms.accountForms import AccountForm
import cloudinary, cloudinary.uploader

@bp_acc.route("/account")
@login_required
def account():
    title = 'Account'
    userID = session.get('user_id')
    data = UserRepo.get_current_user(userID)
    print(data)
    return render_template("account/account.html", title=title, users=data)


# Upload to Cloudinary
def uploadImage(image):
    uploadResult = cloudinary.uploader.upload(image, file="User_photos", eager=[{"width": 500, "height": 500, "crop": "fill"}])
    return uploadResult['secure_url'], uploadResult['eager'][0]['secure_url']

@bp_acc.route("/account/update", methods=['GET', 'POST'])
@login_required
def updateImg():
    userId = session.get('user_id')
    if request.method == 'POST':
        form = AccountForm()
        if form.validate_on_submit():

            if form.imgFile.data:
                ImgUrl, ThumbUrl = uploadImage(form.imgFile.data)
                UserRepo.updateImg(ImgUrl, ThumbUrl, userId)

        return redirect(url_for('bp_acc.account'))

@bp_acc.route("/account/settings", methods=['GET', 'POST'])
@login_required
def settings():
    title = 'Settings'
    userID = session.get('user_id')
    form = AccountForm()
    data = UserRepo.get_current_user(userID)
    if request.method == 'POST':
        if form.validate_on_submit():
            fname = form.fname.data
            lname = form.lname.data
            UserRepo.Updatename(fname, lname, userID)
        return redirect(url_for('bp_acc.settings'))

    return render_template("account/settings.html", title=title, users=data, form=form)