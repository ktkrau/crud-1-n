from flask import Flask, render_template, request, redirect
from flask_app import app
from flask_app.models.users import User
from flask_app.models.classrooms import Classroom


@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template('index.html', users = users)


@app.route('/new')
def new():
    classrooms = Classroom.muestra_salones()
    return render_template('new.html', classrooms=classrooms)


@app.route('/create', methods=['POST'])
def create():
    User.guardar(request.form)
    return redirect('/')