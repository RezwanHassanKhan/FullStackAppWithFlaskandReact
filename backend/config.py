from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#initialise the flask application
app = Flask(__name__)


# Allows Your Frontend to Communicate with Your Backend:
#Prevents CORS-Related Errors
#Enables Cross-Origin Requests:
CORS(app)

##initialise database

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



    