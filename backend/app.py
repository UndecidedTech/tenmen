from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from bson import ObjectId

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql:///root:tenmen69#@3.17.145.132/tenmen"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "User %r>" % self.username

@app.route('/')
def create_objectid():
    a = ObjectId()
    return str(a)

if __name__ == '__main__':
    app.run(debug=True)
