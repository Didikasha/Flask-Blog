from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='_90433cd1c7493b18ea2bbbdd2022a12e_'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db=SQLAlchemy(app)

from app import routes