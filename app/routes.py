from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Altimor'}
    posts = [
        {
            'author': {'username': 'Jorhm'},
            'body': 'Victory at Slakbridge'
        },
        {
            'author': {'username': 'Skrak'},
            'body': 'the Copper Kettle is out of ale!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
