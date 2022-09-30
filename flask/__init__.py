from flask import Flask

app = Flask(__name__, template_folder='foo')

from model import md

app.register_blueprint(md)

from blog import bl

app.register_blueprint(bl)

appSecret = app.config['SECRET_KEY'] = 'fgfgfgfgfg'