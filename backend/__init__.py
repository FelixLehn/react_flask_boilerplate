import datetime
import os
import json 
 
from flask import Flask, Response, request,render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Config")
CORS(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user_table"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email

    @staticmethod 
    def add_user(email):
        db.session.add(User(email))
        db.session.commit()

    @staticmethod
    def get_emails():
        result= db.engine.execute(
            """SELECT u.id,u.email,u.active 
            FROM user_table u
            """
        )
        return json.dumps([dict(r) for r in result])

@app.route("/api")
def index():
    # User.add_user(email="fix@lehner.org")
    todos=User.get_emails()
    return Response(todos, mimetype="application/json", status=200)

@app.route("/hello")
def helloWorld():
    text=json.dumps([{'title':'Hello World!'}])
    return  Response(text, mimetype="application/json", status=200)

@app.route("/")
def my_index():
    return render_template("index.html", flask_token="Hello   world")

app.run(host="0.0.0.0",debug=True)