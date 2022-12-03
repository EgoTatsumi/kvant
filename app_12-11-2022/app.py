from flask import Flask, render_template, url_for, request, redirect
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from forms.link_forms import LinkForm, LinkFormSearch
from data.__models import SqlBase, Link, Category
from flask_migrate import Migrate
import urllib.parse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'protected_by_kvantorium'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres@localhost:5439/my_app"

# Подключение к БД
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)

# Создание таблиц
SqlBase.metadata.create_all(engine)
# Привязка метаданных класса SqlBase к engine
SqlBase.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()

migrate = Migrate(app, engine)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def links():
    report_msg = None
    search_form = LinkFormSearch()
    links = session.query(Link).all()
    if request.method == 'POST':
        dict_search = [(str(key).strip(), str(val).strip()) for key, val in dict(search_form.data).items() if
                       key in ['link', 'title', 'comment'] and val]
        print(dict_search)
        if dict_search:
            pass
        else:
            report_msg = 'Заполните полностью данные'
    return render_template('links.html', links=links, search_form=search_form, report_msg=report_msg)


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
            link = Link(
                link=urllib.parse.unquote(link_form.link.data),
                title=link_form.title.data,
                comment=link_form.comment.data
            )
            session.add(link)
            session.commit()
            return redirect('/link_add')
    return render_template('link_add.html', link_form=link_form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
