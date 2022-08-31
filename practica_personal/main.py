from urllib import response
from flask import Flask, request, make_response, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    dicti = {
        'user_ip' : user_ip,
        'texto': "simple texto"
    }
    response = render_template('/blocks.html', **dicti) ## Los elementos se deben de pasar como un diccionsrio

    return response