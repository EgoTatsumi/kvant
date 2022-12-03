import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

SqlBase = declarative_base()


class Link(SqlBase):
    __tablename__ = 'links'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    link = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    comment = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.Date,
                                     default=datetime.now().date)


# Таблица категорий
class Category(SqlBase):
    __tablename__ = 'categories'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)


# Таблица ассоциаций для связи категорий и ссылок

association_links = sqlalchemy.Table(
    'categories_to_links', SqlBase.metadata,
    sqlalchemy.Column('link_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('links.id')),
    sqlalchemy.Column('category_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('categories.id'))
)
