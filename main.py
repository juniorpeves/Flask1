# Importando las clases de Flask
import os
from flask import request, make_response, redirect, render_template, session, url_for, flash
# from wtforms.fields.simple import SubmitField
import unittest

from flask.helpers import send_from_directory

from app import create_app
from app.forms import LoginForm
from app.firestore_service import *
# Declarando una nueva variable instanciandola con Flask
# Con el parametro de la aplicación

app = create_app()

todos = ['Junior', 'Calo', 'Toño']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    
@app.errorhandler(404)
def not_found(error): 
      return render_template('error_404.html', error=error)
  
@app.errorhandler(500)
def not_found(error): 
      return render_template('error_500.html', error=error)

@app.route('/', methods=['GET'])
def index():
    user_ip = request.remote_addr # request de ip
    
    response = make_response(redirect("/hello")) # Haciendo una redirección desde un response
    session['user_ip'] = user_ip #Clase16 Usando session
    # response.set_cookie('user_ip', user_ip) # Guardando la ip en una cookie
    return response

@app.route('/hello', methods=['GET']) # Usando el decorador con la función route 
def hello():
    user_ip = session.get('user_ip') # request de cookies
    login_form = LoginForm()
    username = session.get('username') # 04 Obteninedo el username desde session
    # Creando un diccionario para pasarlo como contexto de varias variables
    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'login_form': login_form,
        'username': username # 05 Agregandolo al contexto
    }
    
    users=get_users()
    for user in users:
        print (user.id)
        print(user.to_dict()['password']) #Convertir el documentsnapshot a un diccionario
    
    return render_template('hello.html', **context)
    # GET Se envia un diccionario expandido con el **
    
@app.route('/xxx') # Usando el decorador con la función 00route 
def xxx():
    return render_template('xxx.html')

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico', mimetype='image/png')