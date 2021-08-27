from flask import Flask, render_template
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'abc678def987'

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
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ =='__main__':
    app.run(debug=True)