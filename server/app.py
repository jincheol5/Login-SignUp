

from flask import Flask,render_template,request
from db import signup_db

def createAPP():

    app=Flask(__name__)


    

    @app.route('/',methods=["GET"])
    def home():
        return render_template("home.html")

    @app.route('/get_login',methods=['GET'])
    def getLogin():
        return render_template("login.html")

    @app.route('/get_signup',methods=['GET'])
    def getSignUp():
        return render_template("signup.html")

    @app.route('/signup',methods=["POST"])
    def signup():

        userName=request.form.get('name')
        userID=request.form.get('ID')
        userPW=request.form.get('PW')

        signup_db(userName,userID,userPW)

        return userName+" 계정 등록 완료"



    @app.route('/login',methods=["POST"])
    def login():
        return "login"

    

    return app