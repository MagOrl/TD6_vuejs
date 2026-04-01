from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
import os

app = Flask(__name__)

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__), p
        )
    )

cors = CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = (f"sqlite:///{mkpath("../quiz.db")}")
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)