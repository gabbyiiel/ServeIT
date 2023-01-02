from flask import render_template, request, flash, redirect, session
from . import bp_user_db
from ServeIT.models.dbUtils.UserRepo import UserRepo

@bp_user_db.route('/dashboard')
def dashboard():
    if "username" in session:
        username = session["username"]
        title = 'Dashboard'
        fname = UserRepo.get_fname(username)
        if fname:
            return render_template("dashboard/dashboard.html", title=title, fname=fname)
        else:
            return "Error: Could not retrieve user data"
    else:
        return redirect('/login')