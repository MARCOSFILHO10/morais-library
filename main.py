from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if "submit_button" in request.form:
            if ((request.form['username'] == 'Xuxinha') and (request.form['password'] == '123456')):
                print("Login realizado com sucesso!")
                return render_template("home.html")
            else:
                return render_template('login.html') 
    return render_template('login.html')

    