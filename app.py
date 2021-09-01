from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc678def987'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import Post, User

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

if __name__ =='__main__':
    app.run(debug=True)