from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, URL, Length


class LinkForm(FlaskForm):
    link = TextAreaField('Ссылка:', validators=[DataRequired(), URL()])
    title = TextAreaField('Заголовок:', validators=[DataRequired(), Length(max=400)])
    comment = TextAreaField('Комментарий:')

    link_submit = SubmitField()


class LinkFormSearch(FlaskForm):
    link = StringField('Ссылка:')
    title = StringField('Заголовок:')
    Comment = StringField('Комментарий:')
    search_submit = SubmitField('Найти')