from flask import Flask, render_template
app = Flask(__name__)

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
def habout():
    return render_template('about.html', title = 'About')

if __name__ =='__main__':
    app.run(debug=True)