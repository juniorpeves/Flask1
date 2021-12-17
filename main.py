# Importando las clases de Flask
from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Length
# Declarando una nueva variable instanciandola con Flask
# Con el parametro de la aplicación
app = Flask(__name__) 
bootstrap = Bootstrap(app)

todos = ['Junior', 'Calo', 'Toño']
app.config['SECRET_KEY']='Super secreto'

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
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

@app.route('/hello', methods=['GET', 'POST']) # Usando el decorador con la función route 
def hello():
    user_ip = session.get('user_ip') # request de cookies
    login_form = LoginForm()
    username = session.get('username') # 04 Obteninedo el username desde session
    
    # Creando un diccionario para pasarlo como contexto de varias variables
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username # 05 Agregandolo al contexto
    }
    # POST, Si la forma es valida hacemos un redirect
    # 01 Validate_on_submit detecta si la forma es valida en un post
    if login_form.validate_on_submit():
        username = login_form.username.data # 02 Obteninedo el username
        session['username'] = username # 03 Guardandolo en session
        
        flash('Success')
        return redirect(url_for('index'))
    
    return render_template('hello.html', **context)
    # GET Se envia un diccionario expandido con el **
    

@app.route('/xxx') # Usando el decorador con la función 00route 
def xxx():
    return render_template('xxx.html')