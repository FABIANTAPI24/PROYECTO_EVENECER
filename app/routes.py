from flask import render_template
from app import app

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/crear_cuenta')
@app.route('/crear_cuenta.html') #
def crear_cuenta():
    return render_template('crear_cuenta.html')

@app.route('/direccion')
@app.route('/direccion.html')
def direccion():
    return render_template('direccion.html')

@app.route('/iniciar_sesion')
@app.route('/iniciar_sesion.html')
def iniciar_sesion():
    return render_template('iniciar_sesion.html')