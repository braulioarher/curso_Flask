from urllib import response
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__) #Creamos una nueva instacia pasandole el nombre de la aplicacion

todos = ['Comparar cafe', 'Enviar solicitud de compra', 'Entregar video al productor']

@app.route('/') ## se crea esta ruta para redireccionar a route automaticamente
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello') #Definimos la ruta de inicio de nuestra aplicacion con un decorador
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip, 
        'todos': todos
    }
    return render_template('hello.html', **context)