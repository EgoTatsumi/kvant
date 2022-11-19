from flask import Flask, render_template, url_for, request
import sqlalchemy

from forms.link_forms import LinkForm
from data.__models import SqlBase, Link


app = Flask(__name__)
app.config['SECRET_KEY'] = 'protected_by_kvantorium'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres@localhost:5439/my_app"

# Подключение к БД
# engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)

# Создание таблиц
# SqlBase.metadata.create_all(engine)
# Привязка метаданных класса SqlBase к engine
# SqlBase.metadata.bind = engine


@app.route('/')
@app.route('/index')
def links():
    return render_template('links.html')


@app.route('/get_title', methods=['POST', 'GET'])
def get_title():
    print('ЗАПРОС:', request)

    # При отправке методом GET
    link = request.args.get('link')
    btn_text = request.args.get('btn_id')
    print(link)
    print(btn_text)

    # При отправке методом POST
    # request.form.get('link')
    # request.form.get('btn_id')

    # Если ответ не требуется
    # return '', 204

    return 'Заголовок страницы'


@app.route('/link_add', methods=['POST', 'GET'])
def links_manage():
    link_form = LinkForm()
    if request.method == 'POST':
        if link_form.validate_on_submit():
            return f"Форма отправлена: {link_form.data}"
    return render_template('link_add.html', link_form=link_form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
