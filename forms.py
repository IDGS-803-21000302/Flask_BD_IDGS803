from wtforms import Form
from wtforms import StringField, SelectField,RadioField,EmailField,IntegerField
from wtforms import validators


class UsersForm(Form):
    nombre = StringField('nombre',[
        validators.DataRequired(message='el campo es requerido'),
        validators.Length(min=4, max=20, message = 'ingresa nombre valido')
    ])

    apaterno = StringField('apaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.Length( max=20, min=4, message = 'ingresa nombre valido')
    ])

    amaterno = StringField('amaterno',[
        validators.DataRequired(message='el campo es requerido'),
        validators.Length(min=4, max=20, message = 'ingresa nombre valido')
    ])

    edad = IntegerField('edad')

    correo = EmailField('correo',[
        validators.Email(message='Ingrese un corre valido')
    ])
