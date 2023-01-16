from flask import render_template, request, flash, redirect, session, url_for
from . import bp_auth
import functools
from ServeIT.models.dbUtils.UserRepo import UserRepo, College
from .forms.userforms import LoginForm, SignupForm

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not session.get('user_id'):
            return redirect(url_for('bp_auth.login'))

        return view(**kwargs)

    return wrapped_view

@bp_auth.route ('/')
def index():
    title='ServeIT'
    return render_template("home/home.html", title=title)

@bp_auth.route('/about')
def ap_index():
    title = 'About'
    return render_template("home/about.html", title=title)

@bp_auth.route('/services')
def sp_index():
    title = 'Services'
    return render_template("home/services.html", title=title)

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Log In'
    form = LoginForm()
    if session.get('user_id'):
      return redirect('dashboard')
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data 
        result = UserRepo.login(username, password)
        if result is not None and result['code'] == -1:
          form.username.data = username
          if form.username.errors:
            form.username.data = ""
          flash(result['message'])
          return render_template("login/login.html", form=form, title=title)
        else:
          print('Logged in User -', result['user_id'])
          session['user_id'] = result['user_id']

          return redirect('dashboard')
    return render_template("login/login.html", form=form, title=title)

@bp_auth.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@bp_auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    title = 'Sign Up'
    form = SignupForm()
    collegeList = College.college_retrieveAll()
    coursesList = College.courses_retrieveAll()
    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        college = request.form.get('college')
        course = request.form.get('course')
        idnumber = form.idnumber.data
        password = form.password.data
        gender = form.gender.data
        username = form.username.data
        # call signup function and check if it returns an error
        result = UserRepo.signup(username, idnumber, fname, lname, email, college, course, password, gender)
        if result['code'] == -1:
            flash(result['message'])
            # Keep the inputted form data and clear the invalid input fields
            form.fname.data = fname
            form.lname.data = lname
            form.email.data = email
            form.idnumber.data = idnumber
            form.password.data = password
            form.gender.data = gender
            form.username.data = username
            if form.fname.errors:
              form.fname.data = ""
            if form.lname.errors:
              form.lname.data = ""
            if form.email.errors:
              form.email.data = ""
            if form.idnumber.errors:
              form.idnumber.data = ""
            if form.password.errors:
              form.password.data = ""
            if form.gender.errors:
              form.gender.data = ""
            if form.username.errors:
              form.username.data = ""
            return render_template("signup/signup.html", form=form, title=title, colleges=collegeList)
        else:
            return redirect('login')
    return render_template("signup/signup.html", form=form, title=title, collegelist=collegeList, courselist=coursesList)
