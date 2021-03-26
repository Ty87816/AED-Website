from flask import Flask
import json
from app import app, db
from app.models import User
import string
import random


def test_home():
    
    client = app.test_client()
    url = '/'
    response = client.get(url)
    assert response.status_code == 200
    
 
def test_login():
    
    client = app.test_client()
    url = '/login'
    response = client.get(url)
    assert response.status_code == 200
    
def test_register():
    
    client = app.test_client()
    url = '/register'
    response = client.get(url)
    assert response.status_code==200
def test_home():
    
    client = app.test_client()
    url = '/home'
    response = client.get(url)
    assert response.status_code==200
    
def test_event():
    
    client = app.test_client()
    url = '/events'
    response = client.get(url)
    assert response.status_code==200

def test_comment_wall():
    
    client = app.test_client()
    url = '/comments'
    response = client.get(url)
    assert response.status_code==200

def create_new_user():
    username = string.ascii_letters
    temp = string.ascii_letters
    password = ''.join(random.choice(temp) for i in range(10))
    email = string.ascii_letters
    
    data = {}  
    
    data["username"] = ''.join(random.choice(username) for i in range(10))
    data["password"] = password
    data["confirm_password"] = password
    data["email"] = ''.join(random.choice(email) for i in range(10)) + "@gmail.com"
    
    return data
    
def test_register_new_user():
    packet = create_new_user()
    client = app.test_client()
    response = client.post('/register',data=packet)
    
    assert response.status_code==200
    

def test_unique_user():
    packet = create_new_user()
    client = app.test_client()
 
    action = True
    try:
        user = User(username=packet['username'], email=packet['email'], password=packet['password'])
        db.session.add(user)
        db.commit()
        copy = User(username=packet['username'], email=packet['email'], password=packet['password'])
        db.session.add(copy)
    except Exception:
        action = False
    finally:
        assert not action
   
    
    
    
    
    
    
    
    
    