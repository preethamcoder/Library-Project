from flask import Flask, render_template
from flask import request, redirect
from random import randint

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("In the hello world method")
    return render_template('Loginpage1.html')

@app.route('/Loginpage1.html')
def hello_world1():
	return render_template('Loginpage1.html')

@app.route('/create/NewUserPage.html')
def loginreset():
    return render_template('NewUserPage.html')
@app.route('/NewUserPage.html')
def login_function():
    # This is one of returning content from python program to HTML page 
    return render_template('NewUserPage.html')
    # other way is using render_tempalte("<<html file")

@app.route('/loginnext')
def openfil():
    libid = request.form.get("libid")
    pwd = request.form["pwd"]
    print(libid)
    print(pwd)
    if(libid == "1234" and pwd == "passw0rd"): 
            return render_template('success.html')
    else:
            return render_template('error.html')

@app.route('/create/confirm')
def template_render():
    return render_template('Creation_confirmation.html')
    
@app.route('/create/Loginpage1.html')
def template_render1():
    return render_template('Loginpage1.html')
    
#if(__name__ == "main"):
#    hello_world()    