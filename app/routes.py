from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index/')
def index():
    title = 'Home'
    user = {'username': 'David'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers move was so cool!'
        }
    ]
    return render_template('index.html', title=title, user=user, posts=posts)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    title = 'Sign In'
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title=title, form=form)