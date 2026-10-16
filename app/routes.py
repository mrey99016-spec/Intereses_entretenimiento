from flask import Blueprint, render_template, request

routes = Blueprint('routes', __name__)

@routes.route('/')
def inicio():
    return render_template('index.html')

@routes.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    interes = request.form['interes']
    return render_template('gracias.html', nombre=nombre, interes=interes)