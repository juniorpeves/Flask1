# Importando las clases de Flask
from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired
# Declarando una nueva variable instanciandola con Flask
# Con el parametro de la aplicación
app = Flask(__name__) 
bootstrap = Bootstrap(app)

todos = ['Junior', 'Calo', 'Toño']
app.config['SECRET_KEY']='Super secreto'

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error): 
      return render_template('error_404.html', error=error)
  
@app.errorhandler(500)
def not_found(error): 
      return render_template('error_500.html', error=error)
  

@app.route('/')
def index():
    user_ip = request.remote_addr # request de ip
    
    response = make_response(redirect("/hello")) # Haciendo una redirección desde un response
    session['user_ip'] = user_ip #Clase16 Usando session
    # response.set_cookie('user_ip', user_ip) # Guardando la ip en una cookie
    return response

@app.route('/hello') # Usando el decorador con la función 00route 
def hello():
    user_ip = session.get('user_ip') # request de cookies
    # Creando un diccionario para pasarlo como contexto de varias variables
    login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form
    }
    # Se envia un diccionario expandido con el **
    return render_template('hello.html', **context)

@app.route('/xxx') # Usando el decorador con la función 00route 
def xxx():
    return render_template('xxx.html')