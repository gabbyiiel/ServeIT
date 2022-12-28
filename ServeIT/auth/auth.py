from flask import render_template, request, flash, redirect, session, url_for
from flask_login import login_user, login_required, logout_user, current_user
from . import bp_auth
from ServeIT.models.dbUtils.UserRepo import UserRepo
from .forms.loginform import LoginForm

@bp_auth.route ('/')
def index():
    return render_template("home/test.html")

@bp_auth.route('/home', methods=['GET'])
def home():
    return render_template("home/landing.html")

@bp_auth.route('/dashboard')
def dashboard():
    if "username" in session:
        username = session["username"]
        title = 'Dashboard'
        return render_template("users/base.html", title=title)
    else:
        return redirect('/login')

@bp_auth.route('/userprofile')
def userprofile():
    if "username" in session:
        username = session["username"]
        title = 'Profile'
        return render_template("users/userprofile.html", title=title)
    else:
        return redirect('/login')


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
    title = 'Login'
    form = LoginForm()
    username = None

    if session.get('id'):
        return redirect(url_for(".dashboard"))

    if request.method == 'POST':
        if form.validate():
            username = request.form('inputUsername')
            password = request.form('inputPassword')
            user = UserRepo.login(username, password)

        if user:
            session['loggedin'] = True
            session['id'] = user
            session['username'] = username
            return redirect('/dashboard')
        else:
            return "<p> wrong? </p>"
    return render_template("auth/loginpage.html", boolean=True, title=title)

@bp_auth.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect('login')


@bp_auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    title = 'Sign Up'
    if request.method == 'POST':
        firstname = request.form.get('inputFirstname')
        lastname = request.form.get('inputLastname')
        email = request.form.get('inputEmail')
        college = request.form.get('college_select')
        idnumber = request.form.get('inputIdnumber')
        course = request.form.get('course_select')
        password = request.form.get('inputPassword')
        gender = request.form.get('Gender')
        username = request.form.get('inputUsername')
        #function for verification
        if len(password) < 8:
            flash('Password must be at least 8 characters', category='error')
            return redirect('signup')
        else:
            signup = UserRepo.signup(username,idnumber, firstname, lastname, email, course, college, password, gender)
            flash('Account Created', category='success')
            return redirect('login')

    return render_template("auth/signup-page.html", title=title)


