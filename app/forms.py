from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')
    

class TodoForm(FlaskForm):
    description = StringField('Descripcion', validators=[DataRequired()])
    consumo = IntegerField('Consumo en Watts', validators=[DataRequired()])
    tiempo_uso = FloatField('Tiempo de uso promedio diario en horas', validators=[DataRequired(), NumberRange(0.1, 24, 'Ingrese un Valor entre 0.1 y 24 horas')])
    submit = SubmitField('Crear')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')


