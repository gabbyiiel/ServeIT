from flask import render_template, request, flash, redirect, session, url_for
from . import bp_acc
from ServeIT.auth.auth import login_required
from ServeIT.models.dbUtils.UserRepo import UserRepo, College
from ServeIT.models.dbUtils.ServicesRepo import Services
from .forms.accountForms import BasicInfoForm, UserInfoForm, SchoolInfoForm
import cloudinary, cloudinary.uploader

@bp_acc.route("/account")
@login_required
def account():
    title = 'Account'
    userID = session.get('user_id')
    data = UserRepo.get_current_user(userID)
    accept_request = Services.count_user_accepted_requests(userID)
    created_request = Services.count_user_requests(userID)
    college = College.get_user_college(data['college'])
    course= College.get_user_course(data['course'])


    return render_template("account/account.html", title=title, user=data, colleges=college, courses=course, crequest=created_request, arequest=accept_request)


# Upload to Cloudinary
def uploadImage(image):
    uploadResult = cloudinary.uploader.upload(image, file="User_photos", eager=[{"width": 500, "height": 500, "crop": "fill"}])
    return uploadResult['secure_url'], uploadResult['eager'][0]['secure_url']



@bp_acc.route("/account/settings", methods=['GET', 'POST'])
@login_required
def settings():
    title = 'Settings'
    userID = session.get('user_id')
    sform = SchoolInfoForm()
    bform = BasicInfoForm()
    uform = UserInfoForm()
    data = UserRepo.get_current_user(userID)
    ucollege = College.get_user_college(data['college'])
    ucourse= College.get_user_course(data['course'])
    collegelist = College.college_retrieveAll()
    courselist = College.courses_retrieveAll()
    if bform.validate_on_submit() and request.method == 'POST':
        fname = bform.fname.data
        lname = bform.lname.data
        contactnum = bform.contactnum.data
        UserRepo.Updatebasicinfo(fname, lname, contactnum, userID)
        return redirect(url_for('bp_acc.settings'))
    
    if uform.validate_on_submit() and request.method == 'POST':
        if uform.password.data != uform.verify_password.data:
            print("Password does not match")
            return redirect(url_for('bp_acc.settings'))
        username = uform.username.data
        password = uform.password.data
        print(username,password)
        UserRepo.Updateuserinfo(username, password, userID)
        return redirect(url_for('bp_acc.settings'))
    
    if sform.validate_on_submit() and request.method == 'POST':
        idnumber = sform.idnumber.data
        college = request.form.get('college')
        course = request.form.get('course')
        UserRepo.Updateschoolinfo(idnumber, college, course, userID)
        return redirect(url_for('bp_acc.settings'))

    return render_template("account/settings.html", title=title, user=data, sform=sform, bform=bform, uform=uform, colleges=ucollege, collegelist=collegelist, courselist=courselist, courses=ucourse)