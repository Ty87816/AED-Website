from flask import Flask
from flask import request, render_template, url_for, flash, redirect
import json
from form import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'testing_key' 

@app.route('/')
def hello_world():
    title = "PDSP Home"
    return render_template('index.html', title=title)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    reg_form = RegistrationForm()
    log_form = LoginForm()
    if reg_form.validate_on_submit():
        flash(f'Succes for {reg_form.username.data}!','success')
    return render_template('login.html', form=reg_form)

@app.route('/events')
def events():
    return render_template('Events.html')

@app.route('/comments')
def comments():
    return render_template('CommentWall.html')
    
if __name__ == '__main__':
    app.run()
