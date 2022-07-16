from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db" 

db = SQLAlchemy(app)

from .models.Transaction import Transaction
from .models.TransactionType import TransactionType
from . import routes
