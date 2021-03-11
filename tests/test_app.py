from flask import Flask
import json
from ..app import app
import forms

  
def test_home():
    
    client = app.test_client()
    url = '/'

    response = client.get(url)
    
    assert response.status_code == 200
    

