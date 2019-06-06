from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForms

@app.route('/')
@app.route('/index')
def index():
    user = { 'username':'Ameya'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    forms = LoginForms()
    if forms.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(forms.username.data, forms.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=forms) 