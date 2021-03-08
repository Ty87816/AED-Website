from flask import Flask
from flask import request, render_template
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    title = "PDSP Home"
    return render_template('index.html', title=title)
    
@app.route('/login')
def login():
    return render_template('login.html')
        
@app.route('/register')
def register():
    return render_template('register.html')
    
if __name__ == '__main__':
    app.run()
