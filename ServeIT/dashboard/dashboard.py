from flask import render_template, request, flash, redirect, session, url_for
from . import bp_dashboard
from ServeIT.auth.auth import login_required
from ServeIT.models.dbUtils.UserRepo import UserRepo
from ServeIT.models.dbUtils.ServicesRepo import Services
from ServeIT.Services.forms.ServicesForm import ServicesForm
import cloudinary, cloudinary.uploader
from cloudinary.uploader import upload

@bp_dashboard.route('/dashboard')
@login_required
def dashboard():
    userID = session.get('user_id')


    title = 'Dashboard'
    fname = UserRepo.get_fname(userID)
    form = ServicesForm()
    if fname:
        return render_template("dashboard/dashboard.html", title=title, fname=fname, form=form)
    else:
        return "Error: Could not retrieve user data"

    


@bp_dashboard.route('/dashboard/add', methods=['GET', 'POST'])
def add_print_request():
    userID = session.get('user_id')
    if request.method == 'POST':
        form = ServicesForm()
        if form.validate_on_submit():
            printfile = form.printfile.data
            num_copies = form.num_copies.data
            specification = form.specification.data

            fileURL= ''
            if form.printfile.data:
                fileURL = uploadFile(printfile)
            service_name="PR"
            Services.add_service(service_name)
            
            result = Services.add_printing(fileURL,num_copies,specification)
            if result is not None and result['code'] == -1:
                flash(result['message'])
            else:
                redirect('bp_dashboard.dashboard')
        return redirect(url_for('bp_dashboard.dashboard'))
    else:
        flash("You are trying to access a forbidden URL.", "error")
        return redirect(url_for('bp_dashboard.dashboard'))


def uploadFile(file):
    uploadResult = cloudinary.uploader.upload(file, folder="StudenDiri/Print_files")
    return uploadResult['secure_url']