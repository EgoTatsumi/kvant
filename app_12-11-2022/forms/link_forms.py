from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL, Length, InputRequired


class LinkForm(FlaskForm):
    link = TextAreaField('Ссылка:', validators=[DataRequired(), URL()])
    title = TextAreaField('Заголовок:', validators=[DataRequired(), Length(max=400)])
    comment = TextAreaField('Комментарий:')

    link_submit = SubmitField()
