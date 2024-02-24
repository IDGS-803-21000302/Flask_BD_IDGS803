from flask import Flask, render_template, request, flash, Response
from flask_wtf.csrf import CSRFProtect
from flask import redirect
from flask import g
from config import DevelopmentConfig
import forms

from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_fund(e):
    return render_template('404.html'),404


@app.route("/index")
def index():
    escuela="UTL!!!"
    alumnos=["mario","Pedro","Luis","Dario"]
    return render_template("index.html",escuela=escuela,alumnos=alumnos)

@app.route("/alumnos",methods=["GET","POST"])
def alum():
    nom=''
    apa=''
    ama=''
    mensaje=''
    alum_form= forms.UsersForm(request.form)
    if request.method=='POST' and alum_form.validate():
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data

        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)

        print("Nombre: {}".format(nom))
        print("Apa: {}".format(apa))
        print("Ama: {}".format(ama))
        
    return render_template("alumnos.html",form=alum_form,nom=nom,apa=apa,ama=ama)


if __name__== "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)

