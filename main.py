# Importando las clases de Flask
from flask import Flask, request, make_response, redirect

app = Flask(__name__) 
# Declarando una nueva variable instanciandola con Flask
# Con el parametro de la aplicación

@app.route('/')
def index():
    user_ip = request.remote_addr # request de ip
    
    response = make_response(redirect("/hello")) # Haciendo una redirección desde un response
    response.set_cookie('user_ip', user_ip) # Guardando la ip en una cookie
    
    return response

@app.route('/hello') # Usando el decorador con la función 00route 
def hello():
    user_ip = request.cookies.get('user_ip') # request de cookies
    
    return "Hello World Junior, tu IP es {}".format(user_ip)