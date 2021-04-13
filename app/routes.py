from flask import request, render_template, url_for, flash, redirect
from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename


@app.route('/')
@app.route('/home')
def home():
    title = "PDSP Home"
    return render_template('calendar.html', title=title)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    log_form = LoginForm()
    if log_form.validate_on_submit():
        user = User.query.filter_by(username=log_form.username.data).first()
        
        if user and user.password == log_form.password.data:
            flash(f'{log_form.username.data} logged on!', 'success')
            login_user(user)
            return redirect(url_for('home'))
    
    
    return render_template('login.html', form=log_form)    

@app.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    
    return render_template('registration.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@app.route('/events', methods=['GET', 'POST'])
def events():
    return render_template('Events.html')

@app.route('/comments')
def comments():
    return render_template('CommentWall.html')
