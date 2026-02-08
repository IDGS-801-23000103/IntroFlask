from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email, Length, Regexp, NumberRange


class UserForm(FlaskForm):

    matricula = IntegerField(
        "Matrícula",
        validators=[
            DataRequired(message="La matrícula es obligatoria"),
            NumberRange(min=1, message="Matrícula no válida")
        ]
    )

    nombre = StringField(
        "Nombre",
        validators=[
            DataRequired(message="El nombre es obligatorio"),
            Length(min=3, message="Mínimo 3 caracteres"),
            Regexp("^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$",
                   message="Solo letras")
        ]
    )

    apaterno = StringField(
        "Apellido Paterno",
        validators=[
            DataRequired(message="Campo obligatorio"),
            Regexp("^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$",
                   message="Solo letras")
        ]
    )

    amaterno = StringField(
        "Apellido Materno",
        validators=[
            DataRequired(message="Campo obligatorio"),
            Regexp("^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$",
                   message="Solo letras")
        ]
    )

    correo = EmailField(
        "Correo Electrónico",
        validators=[
            DataRequired(message="Correo obligatorio"),
            Email(message="Correo no válido")
        ]
    )
