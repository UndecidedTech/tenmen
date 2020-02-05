from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from bson import ObjectId
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql:///root:tenmen69#@3.17.145.132/tenmen"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

socketio = SocketIO(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "User %r>" % self.username

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
@app.route('/user', methods=['POST'])
def addUser():
    id = create_objectid();
    username = request.json['username']
    email = request.json['email']
        # hash password 
        # include firstname and lastname
        
    new_user = User(id, username, email)

    db.session.add(new_user)
    db.session.commit()
    return new_user

@app.route('/', methods=["GET"])
def create_objectid():
    a = ObjectId()
    return str(a)

if __name__ == '__main__':
    app.run(debug=True)


@socketio.on("connect")
def handle_connect():
    socketio.emit("recieved message: ", {"data": "connected"})