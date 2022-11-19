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
