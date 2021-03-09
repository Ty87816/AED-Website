from flask import Flask
from flask import request, render_template
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    title = "PDSP Home"
    return render_template('index.html', title=title)
    
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    reg_form = RegistrationForm()
    log_form = LoginForm()
    if reg_form.validate_on_submit()
        flash('f'Succes for {form.username.data}!','success')
    return render_template('login.html', form=reg_form)
    
if __name__ == '__main__':
    app.run()
