from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from html_model import LoginForm, SignUpForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

controller = Flask(__name__)
#istance of a Flask Class used to generate the app to be launched
#__name__ is a global variable and it stays for this module: app
controller.config['SECRET_KEY'] = 'reallysecretkey'
#forms don't work without secret key
controller.config['SQLALCHEMY_DATABASE_URI']='sqlite:///website.db'


db=SQLAlchemy(controller)

@controller.before_first_request
def setup_all():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(controller)
login_manager.login_view = 'login'

@controller.route('/homepage')
#route is a decorator
#URL match, it says if the url is '/' shows this stuff below
#It invokes add_url_route()
#It has the attribute methods that can be GET, POST and both
#methods=['GET', 'POST']
def home():
    return render_template('index.html')
#RENDERING: it is the process that replaces the variables with actual values gotten by http request
#and retunrs a final string response

@controller.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form =form)

@controller.route('/signup', methods=['POST','GET'])
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)

@controller.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    controller.run(debug=True, use_reloader=True)
#It runs the app on the local flask server
# it is only intended for a debug purpose
#default host: 127.0.0.1, default port: 5000, use SERVER_NAME variable to change these settings

