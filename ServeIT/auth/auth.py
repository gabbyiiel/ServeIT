from flask import render_template, request, flash, redirect, session
from . import bp_auth
from ServeIT.models.dbUtils.UserRepo import UserRepo
from .forms.userforms import LoginForm, SignupForm


@bp_auth.route ('/')
def index():
    return render_template("home/test.html")

@bp_auth.route('/about')
def ap_index():
    title = 'About'
    return render_template("aboutpage/base.html", title=title)

@bp_auth.route('/services')
def sp_index():
    title = 'Services'
    return render_template("servicespage/base.html", title=title)

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Log In'
    form = LoginForm()
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
          
          session['logged_in'] = True
          session['username'] = username
          return redirect('dashboard')
    return render_template("login/login.html", form=form, title=title)

@bp_auth.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect('/')


@bp_auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    title = 'Sign Up'
    form = SignupForm()
    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        college = form.college.data
        idnumber = form.idnumber.data
        course = form.course.data
        password = form.password.data
        gender = form.gender.data
        username = form.username.data
        # call signup function and check if it returns an error
        result = UserRepo.signup(username, idnumber, fname, lname, email, course, college, password, gender)
        if result['code'] == -1:
            flash(result['message'])
            # Keep the inputted form data and clear the invalid input fields
            form.fname.data = fname
            form.lname.data = lname
            form.email.data = email
            form.college.data = college
            form.idnumber.data = idnumber
            form.course.data = course
            form.password.data = password
            form.gender.data = gender
            form.username.data = username
            if form.fname.errors:
              form.fname.data = ""
            if form.lname.errors:
              form.lname.data = ""
            if form.email.errors:
              form.email.data = ""
            if form.college.errors:
              form.college.data = ""
            if form.idnumber.errors:
              form.idnumber.data = ""
            if form.course.errors:
              form.course.data = ""
            if form.password.errors:
              form.password.data = ""
            if form.gender.errors:
              form.gender.data = ""
            if form.username.errors:
              form.username.data = ""
            return render_template("signup/signup.html", form=form, title=title)
        else:
            return redirect('login')
    return render_template("signup/signup.html", form=form, title=title)
