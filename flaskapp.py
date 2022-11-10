from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import psycopg2

db = SQLAlchemy()
# app object (literally web server)
app = Flask(__name__)



# Adding PostgreSQL database URI to a config
app.config['SQLALCHEMY_DATABASE_URI'] = r"postgresql://postgres:Bkazbekov20@localhost:5432/shop"

with app.app_context():
    db.init_app(app)
# Used to create a session object
# user can look at the session contents, but can’t modify it
# unless they know the secret key, so make sure to set that to something complex and unguessable.
app.config['SECRET_KEY']="my secret key here"