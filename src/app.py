#Realizado por Juliana Castillo Araujo
#Parcial 2 
#19 de abril 2024

from flask import Flask, render_template, request, redirect, url_for
from config import *
from productos import Productos


con_bd = conexion()

app = Flask(__name__)

@app.route('/')
def index():
    coleccion =con_bd['Productos']
    ProductosRegistrados =  coleccion.find()
    return render_template('index.html', productos = ProductosRegistrados)

@app.route('/guardar_productos', methods =['POST'])
def agregarPersona():
    coleccion =con_bd['Productos']
    nombre_producto =request.form['nombre_producto']
    valor_producto =request.form['valor_producto']
    cantidad_producto= request.form['cantidad_producto']
    email= request.form['email']
    password= request.form['password']

    if nombre_producto and valor_producto and cantidad_producto and email and password:
        objproducto= Productos(nombre_producto,valor_producto,cantidad_producto,email,password)
        coleccion.insert_one(objproducto.formato_doc())
        return redirect(url_for('index'))

@app.route('/eliminar_productos/<string:nombre_producto>')
def eliminar(nombre_producto):
    coleccion = con_bd['Productos']
    coleccion.delete_one({'nombre': nombre_producto})
    return redirect(url_for('index'))

@app.route('/editar_productos/<string:nombre_producto>', methods=['POST'])
def  editar(nombre_producto):
    coleccion =con_bd['Productos']
    nombre_producto =request.form['nombre_producto']
    valor_producto =request.form['valor_producto']
    cantidad_producto= request.form['cantidad_producto']
    email= request.form['email']
    password= request.form['password']
    
    if nombre_producto and valor_producto and cantidad_producto and email and password:
        coleccion.update_one({'nombre':nombre_producto},{'$set':{'nombre_producto': nombre_producto,'valor_producto':valor_producto, 'cantidad_producto': cantidad_producto}, 'email':email, 'password': password})
        return redirect(url_for('index'))

    else:
        return"Valor incorrecto, intente de nuevo"

if __name__=='__main__':
    app.run(debug=True)