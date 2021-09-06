from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

posts = [
    {
        'author':'Mileniandi',
        'title':'Dummy Post 1',
        'content':'First post content',
        'date_posted':'August 26, 2020'
    },
    {
        'author':'Erika Marina',
        'title':'Dummy Post 2',
        'content':'Second post content',
        'date_posted':'August 27, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and form.password.data == '12345':
            flash(f"Welcome {form.email.data}!", "success")
            return redirect(url_for('home'))
        else :
            flash(f"Login Unsuccesful. Please check email and password", "danger")    
    return render_template('login.html', title='Login', form=form)