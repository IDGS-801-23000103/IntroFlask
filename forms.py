from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email, Length, Regexp, NumberRange


class UserForm(FlaskForm):
    matricula = IntegerField(
        "Matricula",
        validators=[
            DataRequired(message="La matrícula es obligatoria"),
            NumberRange(min=1, message="Ingrese una matrícula válida")
        ]
    )

    nombre = StringField(
        "Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio"),
            Length(min=3, message="El nombre debe tener al menos 3 caracteres"),
            Regexp("^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$",
                message="El nombre solo debe contener letras")
        ]
    )

    apaterno = StringField(
        "Apellido Paterno",
        validators=[
            DataRequired(message="El apellido paterno es obligatorio"),
            Regexp("^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$",
                message="El apellido paterno solo debe contener letras")
        ]
    )

    amaterno = StringField(
        "Apellido Materno",
        validators=[
            DataRequired(message="El apellido materno es obligatorio"),
            Regexp("^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$",
                message="El apellido materno solo debe contener letras")
        ]
    )

    correo = EmailField(
        "Correo",
        validators=[
            DataRequired(message="El correo es obligatorio"),
            Email(message="Ingrese un correo electrónico válido")
        ]
    )