from flask import request, render_template
import json



def configure_routes(app):

    @app.route('/')
    def hello_world():
        return render_template('index.html')
    
    @app.route('/blog')
    def blog():
        return ('blog')
        
    @app.route('/about')
    def about():
        return('about')