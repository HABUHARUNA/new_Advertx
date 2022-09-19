from flask import Flask
from flask_sqlalchemy import SQLAlchemy


main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
main.config['SECRET_KEY'] = 'd7b7b2a1da1484fcc4ccb0b07fec33d6'
db = SQLAlchemy(main)

from advertx import routes