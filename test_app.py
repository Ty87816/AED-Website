from flask import Flask
import json
from ..app import app


  
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
    assert response.get_data() != b'blug'