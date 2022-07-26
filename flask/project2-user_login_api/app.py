from email.policy import default
from flask import Flask, request
import json
from flask_sqlalchemy import SQLAlchemy
from requests import session
from sqlalchemy import Column, String, Integer, ForeignKey, true, exists
import datetime
import base64
import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://hkm:Hkmcs123!@localhost/training"

db=SQLAlchemy(app)

class User(db.Model):
    x=datetime.datetime.now()
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    pwd = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime, default=x)
    updated_at = db.Column(db.DateTime, default=x)
    sessions = db.relationship('Sess', backref='user',lazy='dynamic')

    def __init__(self, username, pwd, email):
        self.username = username
        self.pwd = pwd
        self.email = email

    def chkPwd(self,passwd):
        if(self.pwd == passwd):
            return 1
        else:
            return 0

class Sess(db.Model):
    x=datetime.datetime.now()

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, ForeignKey(User.id))
    session_token = db.Column(db.String(200), unique=True)
    status = db.Column(db.Integer, default=1)
    created_at = db.Column(db.String(200), default=x)
    updated_at = db.Column(db.String(200), default=x)

    def __init__(self,uidIO, session_token, status):
        self.uid = uidIO
        self.session_token = session_token
        self.status = status


#*********************************************************EXTERNAL FUNCTIONS***********************************************************
def generate_token(userId):
    #Generate token on login
    a = str(datetime.datetime.now())
    b = str(userId)
    c = (a+b).encode("ascii")
    d = str(base64.b64encode(c))
    #print(type(str(base64.b64encode(c))),file=sys.stdout)
    return d

def displayUserTable(uid):
    #SELECT username,email from user where username=uname; 
    query = User.query.filter_by(id = uid).first()
    return "{'User ID': '{0}', 'Username': '{1}', 'Email id': '{2}', 'Password': {3}}".format(query.id, query.username, query.email, query.pwd)

def displaySessTable(id):
    query = Sess.query.filter_by(uid = id).first()
    return "{'ID': '{0}', 'User ID': '{1}', 'Session Token': '{2}', 'Status': {3}}".format(query.id, query.uid, query.session_token, query.status)

def signupUser(uname,email,pwd):
    user = User(uname,pwd,email)
    try:
        db.create_all()
        db.session.add(user)
        db.session.commit()
        db.session.flush()
    except:
        return "{'Error': 'Invalid input!'}"
    return "Successfully created! Please login now..."

def generate_session(uid):
    token = generate_token(uid)
    sess = Sess(uid, token, 1)
    try:
        db.create_all()
        db.session.add(sess)
        db.session.commit()
        db.session.flush()
    except:
        pass
    if(sess):
        return 1
    else:
        return 0

def login(uname,pwd):
    test = User.query.filter_by(username=uname).first()
    uid = int(test.id)
    if uid is not None:
        try:
            res = test.chkPwd(pwd)
            if(res):
                generate_session(uid)
                return "Logged in"
            else:
                return "Incorrect password"
        except:
            return "Error: Please verify and try again"
    else:
        return "Enter a valid username!"

def close_session(a):
    try:
        query = Sess.query.filter_by(uid = a).first()
        query.status = 0
        db.session.commit()
        return "Successfully logged out!"
    except:
        return "Error!"

#*********************************************************************************************************************************

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/login', methods=['POST'])
def login_page():
    data = request.get_json()
    uname = data["uname"]
    pwd = data["pwd"]
    return login(uname,pwd)

@app.route('/signup',methods=['POST'])
def signup():
    data = request.get_json()
    uname = data["uname"]
    email = data["email"]
    pwd = data["pwd"]
    if len(uname)==0 or len(email)==0 or len(pwd)==0:
        return "{'Error': 'Invalid input!'}"
    else:
        return signupUser(uname,email,pwd)

@app.route('/logout/<uid>')
def logout(uid):
    return close_session(uid)

@app.route('/user/')
def user():
    sess = Sess.query.filter_by(status=1).first()
    uid = sess.uid
    return displayUserTable(uid)

@app.route('/session/')
def sess():
    sess = Sess.query.filter_by(status=1).first()
    uid = sess.uid
    return displaySessTable(uid)


if __name__=='__main__':
    app.run(debug=true)
