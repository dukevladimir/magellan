import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# App initialisation
app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = "harkonnen"

# App configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']  = \
	'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class ChatForm(FlaskForm):
	sentence = StringField("Say something:",validators = [DataRequired()])
	submit = SubmitField('Submit')

# Routing definitions
@app.route('/',methods = ['GET','POST'])
def index():
	form = ChatForm()
	#chats  = Conversation.query.all()
	if form.validate_on_submit():
		chat = Conversation(phrase = form.sentence.data,speaker = 1)
		response = handler()
		db.session.add(chat)
		db.session.add(response)
		db.session.commit()
		form.sentence.data = ""
	chats  = Conversation.query.all()
	return render_template('index.html',chats = chats,form=form)

# Database definition
class Conversation(db.Model):
	__tablename__='Conversations'
	id = db.Column(db.Integer,primary_key=True)
	phrase = db.Column(db.String(64))
	speaker = db.Column(db.Integer)

def handler():
	# This is where the magic happens!
	return Conversation(phrase = "response", speaker =2 )