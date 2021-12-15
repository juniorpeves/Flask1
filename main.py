# Importando las clases de Flask
from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

# Declarando una nueva variable instanciandola con Flask
# Con el parametro de la aplicación
app = Flask(__name__) 
bootstrap = Bootstrap(app)

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
    response.set_cookie('user_ip', user_ip) # Guardando la ip en una cookie
    
    return response

todos = ['Junior', 'Calo', 'Toño']

@app.route('/hello') # Usando el decorador con la función 00route 
def hello():
    user_ip = request.cookies.get('user_ip') # request de cookies
    # Creando un diccionario para pasarlo como contexto de varias variables
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    # Se envia un diccionario expandido con el **
    return render_template('hello.html', **context)

@app.route('/xxx') # Usando el decorador con la función 00route 
def xxx():
    return render_template('xxx.html')