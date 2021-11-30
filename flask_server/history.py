import functools
from .plataformas import informacion_contacto, informacion_covid, texto_simple, decode_contacto, decode_vacuna, decode_texto



from datetime import datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/decode_menu/decode_nombre', methods=['GET'])
def decode_nombre():
    datos = decode_contacto()
    print(datos)
    return render_template("/decode_nombre.html", datos = datos)

@bp.route('/decode_menu/decode_texto', methods=['GET'])
def decode_text():
    datos = decode_texto()
    print(datos)
    return render_template("/decode_text.html", datos = datos)

@bp.route('/decode_menu/decode_covid', methods=['GET'])
def decode_vac():
    datos = decode_vacuna()
    print(datos)
    return render_template("/decode_covid.html", datos = datos)

@bp.route('/generate_menu', methods=['GET'])
def generate_menu():
    if request.method == 'GET':
        return render_template("/generate_menu.html")

@bp.route('/decode_menu', methods=['GET'])
def decode_menu():
    if request.method == 'GET':
        return render_template("/decode_menu.html")

@bp.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template("home.html")

@bp.route('/generate_menu/formulario_nombre', methods=['GET', 'POST'])
def formulario_nombre():
    completo = False
    if request.method == 'GET':
        completo = False
        return render_template("formulario_nombre.html", completo=completo)
    if request.method == 'POST':
        username = request.form['username']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        telefono = request.form['telefono']
        informacion_contacto(username, apellido, cedula, telefono)
        completo = True
        return render_template("formulario_nombre.html", completo=completo)

@bp.route('/generate_menu/formulario_texto', methods=['GET', 'POST'])
def formulario_texto():
    if request.method == 'GET':
        return render_template("formulario_texto.html")
    if request.method == 'POST':
        username = request.form['username']
        texto_simple(username)
        completo = True
        return render_template("formulario_texto.html", completo=completo)

@bp.route('/generate_menu/formulario_covid', methods=['GET', 'POST'])
def formulario_covid():
    if request.method == 'GET':
        return render_template("formulario_covid.html")
    if request.method == 'POST':
        dosis1 = request.form['dosis1']
        nombre1 = request.form['nombre1']
        lote1 = request.form['lote1']
        dosis2 = request.form['dosis2']
        nombre2 = request.form['nombre2']
        lote2 = request.form['lote2']
        informacion_covid(dosis1, nombre1, lote1, dosis2, nombre2, lote2)
        completo = True
        return render_template("formulario_covid.html", completo=completo)
