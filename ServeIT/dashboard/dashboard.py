from flask import render_template, request, flash, redirect, session
from . import db_user


@db_user.route('/dashboard')
def dashboard():
    if "username" in session:
        username = session["username"]
        title = 'Dashboard'
        return render_template("dashboard/dashboard.html", title=title)
    else:
        return redirect('/login')