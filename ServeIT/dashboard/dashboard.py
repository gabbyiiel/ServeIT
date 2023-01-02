from flask import render_template, request, flash, redirect, session, url_for
from . import bp_user_db
from ServeIT.models.dbUtils.UserRepo import UserRepo
from ServeIT.models.dbUtils.ServicesRepo import Services
from ServeIT.Services.forms.ServicesForm import ServicesForm
import cloudinary, cloudinary.uploader
from cloudinary.uploader import upload

@bp_user_db.route('/dashboard')
def dashboard():
    if "username" in session:
        username = session["username"]
        title = 'Dashboard'
        fname = UserRepo.get_fname(username)
        form = ServicesForm()
        if fname:
            return render_template("dashboard/dashboard.html", title=title, fname=fname, form=form)
        else:
            return "Error: Could not retrieve user data"
    else:
        return redirect('/login')

@bp_user_db.route('/dashboard/add', methods=['GET', 'POST'])
def add_request():
    if request.method == 'POST':
        form = ServicesForm()
        if form.validate_on_submit():
            printfile = form.printfile.data
            num_copies = form.num_copies.data
            specification = form.specification.data
            
            fileURL= ''
            if form.printfile.data:
                fileURL = upload(printfile)

            result = Services.add_print_request()
            if 1 in result:
                flash(f"'{result[1]} {result[2]}' has been successfully added.", "success")
            else:
                flash(f"{result[1]}", "error")
        return redirect(url_for('dashboard'))
    else:
        flash("You are trying to access a forbidden URL.", "error")
        return redirect(url_for('dashboard'))


