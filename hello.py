from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)

# External libraries
bootstrap = Bootstrap(app)
moment = Moment(app)

# @app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.set_cookie('answer', '42')

    return response


# @app.route('/user/<name>')
def user(name):
    dict_prueba = {}
    dict_prueba["somekey"] = 'somevalue'
    some_list = ["ale","maxi","simon"]

    current_time = datetime.now()
    
    return render_template('user.html', current_time = current_time, name=name, dict_prueba=dict_prueba, some_list=some_list)


# @app.route('/delete-cookie')
def delete_cookie():
    response = make_response('<h1>Cookie Deleted</h1>')
    response.delete_cookie('answer')
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




# Routing 
app.add_url_rule('/',"index",index)
app.add_url_rule('/user/<name>',"user",user)
app.add_url_rule('/delete-cookie',"delete-cookie",delete_cookie)