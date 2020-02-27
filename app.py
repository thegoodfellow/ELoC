###################### APP SET UP#################################

from flask import Flask

app = Flask(__name__)
#istance of a Flask Class used to generate the app to be launched
#__name__ is a global variable and it stays for this module: app

app.config['SECRET_KEY'] = 'reallysecretkey'
#Flask-Login uses sessions...without secretkey it would give an error message
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///website.db'

##################################################################

####################### DB SET UP ################################

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(app)



@app.before_first_request #a decorator that create the tables..first of all
def create_all_tables():
    db.create_all()

db.init_app(app) #????????????



from flask_login import LoginManager

#SESSION MANAGEMEMENT set up
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#################################################################

####################### DB MODEL ################################
from flask_login import UserMixin

#If User does not inherit UserMixin the app won't work (error:the class User does not have the attribute is active)
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    #the UserMixin class has a id attrubute that muts be ovverride
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True, nullable=True)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(30),nullable=True)
    surname = db.Column(db.String(30), nullable=True)
    gender = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        return "<User %r>" % self.name

class Tutor(User):
    degree = db.Column(db.String)


###############################################################

####################### ROUTES ################################

from flask import render_template, url_for, redirect

@app.route('/homepage')
#route is a decorator
#URL match, it says if the url is '/' shows this stuff below
#It invokes add_url_route()
#It has the attribute methods that can be GET, POST and both
#methods=['GET', 'POST']
def home():
    return render_template('index.html')
#RENDERING: it is the process that replaces the variables with actual values gotten by http request
#and retunrs a final string response

@app.route('/search')
def seek():
    tts = User.query.filter_by().all()
    return render_template('search.html', tutors= tts)

from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app) #encryption handler

from forms import LoginForm
from datetime import timedelta
from flask_login import login_user, logout_user, current_user

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        dur_time =timedelta(minutes=1)
        tmp_user=User.query.filter_by(username=form.username.data).first()
        if tmp_user and bcrypt.check_password_hash(tmp_user.password, form.password.data):
            login_user(user=tmp_user, duration=dur_time)
            return redirect(url_for('home'))
    return render_template('login.html', form =form)

from forms import SignUpForm, CompleteSignUpForm

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('completeSignup'))

    return render_template('signup.html', form=form)

@app.route('/completeSignup', methods=['POST', 'GET'])
def signup():
    form = CompleteSignUpForm()
    return render_template('completeSignup.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

from flask_login import login_required

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

###############################################################


####################### LOUNCH APP (DEBUG=ON) #################

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
#It runs the app on the local flask server
# it is only intended for a debug purpose
#default host: 127.0.0.1, default port: 5000, use SERVER_NAME variable to change these settings

###############################################################