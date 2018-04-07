import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#from auth.forms import LoginForm
#from flask_login import login_required
#from flask_login import LoginManager

# App initialisation
app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# App configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']  = \
	'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'hard to guess string'
#login_manager = LoginManager()
#login_manager.login_view = 'auth.login'


# Routing definitions
@app.route('/')
def index():
	return render_template('index.html')

# Database definition
class Conversation(db.Model):
	__tablename__='Conversations'
	id = db.Column(db.Integer,primary_key=True)
	phrase = db.Column(db.String(64))
	speaker = db.Column(db.Integer)