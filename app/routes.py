from flask import request, render_template, url_for, flash, redirect, send_file
from app import app, db
from app.models import User, Events, Attendance, Comments
from app.forms import LoginForm, RegistrationForm, AttendanceForm
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
from datetime import datetime




def isAdmin():
    return current_user.is_admin

@app.route('/')
@app.route('/home')
@login_required
def home():
    title = "PDSP Home"
    events = Events().query.all()
    calendar = []
    for event in events:
        calendar.append(event)
    if isAdmin():
        return render_template('calendar.html', title=title,calendar=calendar)
    else:
       return render_template('user-calendar.html', title=title,calendar=calendar)

@app.route('/addEvent', methods=['GET', 'POST'])
def addEvent():
    
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        info = request.form['description']
        event = Events(event=title,start=start,end=end, description=info);
        db.session.add(event)
        db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/deleteEvent', methods=['GET', 'POST'])
def deleteEvent():
    if request.method == 'POST':
        id = request.form['id']
        event = Events.query.filter_by(id=id).one()
        db.session.delete(event)
        db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/udpateEvent', methods=['GET', 'POST'])
def udpateEvent():
    if request.method == 'POST':
        
        start = request.form['start']
        end = request.form['end']
        
        event = Events(start=start,end=end);
        db.session.add(event)
        db.session.commit()
        
    return redirect(url_for('home'))    

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
@login_required
def events():
    events = Events().query.all()
    posts = []
    for event in events:
        posts.append(event)
    if request.method == 'POST':
        for post in posts:
            if post.event in request.form['submit_button']:
                return redirect(url_for("attendance", event=post.event))
            
    return render_template('Events.html',posts=posts)
 

def getSubmissions(fname, lname, event):
    
    if len(fname) != 0 and len(lname) !=0 and len(event) != 0:
        return Attendance.query.filter_by(event=event, f_name=fname, l_name=lname)
    elif len(fname) == 0 and len(lname) == 0 and len(event) != 0:
        return Attendance.query.filter_by(event=event)
    elif len(fname) != 0 and len(lname) != 0 and len(event) == 0:
        return Attendance.query.filter_by(f_name=fname, l_name=lname)
    elif len(fname) == 0 and len(lname) != 0 and len(event) == 0:
        return Attendance.query.filter_by(l_name=lname)
    elif len(fname) != 0 and len(lname) == 0 and len(event) == 0:
        return Attendance.query.filter_by(f_name=fname)
    elif len(fname) == 0 and len(lname) != 0 and len(event) != 0:
        return Attendance.query.filter_by(l_name=lname, event=event)
    elif len(fname) != 0 and len(lname) == 0 and len(event) != 0:
        return Attendance.query.filter_by(f_name=fname, event=event)
    else:
        return Attendance().query.all()


 
@app.route('/admin', methods=['GET', 'POST'])   
@login_required
def admin():
    events = Events().query.all()
    submissions = []
    if request.method == 'POST':
        if request.form['submit'] == 'Search':
            first = request.form['f_name']
            last = request.form['l_name']
            selectedEvent = request.form['events']
            submissions = getSubmissions(fname=first,lname=last,event=selectedEvent)
            return render_template('admin-panel.html', events=events, submissions=submissions)
        elif request.form['submit'] == 'Download File':
            filepath = 'uploads/'
            file = request.form['url']
            filepath = filepath + file
            flash(f'filepath')
            try:
                return send_file(filepath, attachment_filename=file)
            except Exception as e:
                return str(e)
    return render_template('admin-panel.html', events=events)

@app.route('/<event>', methods=['GET', 'POST'])
@login_required
def attendance(event):
    form = AttendanceForm()
    if form.validate_on_submit():
        flash(f'Document Uploaded for {form.f_name.data}!', 'success')
        filename = secure_filename(form.doc.data.filename)
        form.doc.data.save('app/uploads/' + filename)
        now = datetime.now().time()
        attend = Attendance(event=event,file_url=filename,f_name=form.f_name.data, l_name=form.l_name.data, timestamp=now.strftime('%I:%M'))
        db.session.add(attend)
        db.session.commit()
        return redirect(url_for('events'))
    return render_template('attendance.html',form=form)



@app.route('/comments', methods=['GET', 'POST'])
@login_required
def comments():
    comments = Comments().query.all()
    if request.method == 'POST':
        if request.form['submit'] == 'Comment':
            message = request.form['message']
            now = datetime.now()
            comment = Comments(username=current_user.username, message=message, timestamp=now)
            db.session.add(comment)
            db.session.commit()
            comments = Comments().query.all()
            return redirect(url_for('comments',comments=comment))
        elif request.form['submit'] == 'Delete Comment':
            id = request.form['id']
            comment = Comments.query.filter_by(id=id).one()
            db.session.delete(comment)
            db.session.commit()
            comments = Comments().query.all()
            return redirect(url_for('comments',comments=comment))

    return render_template('CommentWall.html', comments=comments)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
