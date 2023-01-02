from flask import render_template, request, flash, redirect, session, url_for
from . import bp_acc
from ServeIT.models.dbUtils.UserRepo import UserRepo
from .forms.accountForms import UpdatePhoto, UpdateForm
import cloudinary, cloudinary.uploader

@bp_acc.route("/account")
def account():
    if "username" in session:
        username = session["username"]
        title = 'Dashboard'
        fname = UserRepo.get_fname(username)
        if fname:
            return render_template("account/account.html", title=title, fname=fname)
        else:
            return "Error: Could not retrieve user data"
    else:
        return redirect('/login')

# Upload to Cloudinary
def uploadImage(image):
    uploadResult = cloudinary.uploader.upload(image, file="User_photos", eager=[{"width": 500, "height": 500, "crop": "fill"}])
    return uploadResult['secure_url'], uploadResult['eager'][0]['secure_url']


@bp_acc.route('/account/settings',methods=['GET', 'POST'])
def update_account():
    updateform = UpdateForm()
    if updateform.validate_on_submit():
        fname = updateform.fname.data
        lname = updateform.lname.data
        email = updateform.email.data
        college = updateform.college.data
        idnumber = updateform.idnumber.data
        course = updateform.course.data
        password = updateform.password.data
        gender = updateform.gender.data
        username = updateform.username.data