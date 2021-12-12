from flask import Flask # Importando la clase Flask

app = Flask(__name__) 
# Declarando una nueva variable instanciandola con Flask
# Con el parametro de la aplicación


@app.route('/') # Usando el decorador con la función 00route 
def home():
    return "Hello World Flask"