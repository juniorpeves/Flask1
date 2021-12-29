# app/auth/views.py
from flask import render_template, session, redirect,flash, url_for
from app.forms import LoginForm

from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form' : login_form
    }
    # POST, Si la forma es valida hacemos un redirect
    # 01 Validate_on_submit detecta si la forma es valida en un post
    if login_form.validate_on_submit():
        username = login_form.username.data # 02 Obteninedo el username
        session['username'] = username # 03 Guardandolo en session
        
        flash('Success')
        return redirect(url_for('index'))
    
    return render_template('login.html', **context)