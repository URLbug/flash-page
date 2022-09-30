from flask_sqlalchemy import SQLAlchemy

from __init__ import app

dbb = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:hello@localhost/foopage"
app.config[" SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class User(dbb.Model):
    id = dbb.Column(dbb.Integer, primary_key=True)
    username = dbb.Column(dbb.String(500), index=True, unique=True, nullable=False)
    email = dbb.Column(dbb.String(500), unique=True, nullable=False)
    password = dbb.Column(dbb.String(500))

    def __repr__(self):
        return f'<users {self.id}>'


class Blog(dbb.Model):
    id = dbb.Column(dbb.Integer,primary_key=True)
    username = dbb.Column(dbb.String(500))
    blogs = dbb.Column(dbb.String(500))

    def __repr__(self):
        return f'<blogs {self.id}>'


with app.app_context():
    dbb.create_all()
