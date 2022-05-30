from flask import Flask,redirect,url_for,render_template,session,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,EmailField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,length
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb.db'
db=SQLAlchemy(app)
app.config['SECRET_KEY']='AAAAAAAAAAA'
class loginForm(FlaskForm):
    username=StringField('Username : ',validators=[DataRequired(),length(min=3,max=10)])
    password=PasswordField('Password : ',validators=[DataRequired(),length(min=2,max=10)])
    submit=SubmitField('Login ',validators=[DataRequired()])
class signForm(FlaskForm):
    username=StringField('Username : ',validators=[DataRequired(),length(min=3,max=10)])
    email=EmailField('Email : ',validators=[DataRequired(),Email()])
    password=PasswordField('Password : ',validators=[DataRequired(),length(min=2,max=10)])
    confermpassword=PasswordField('Conferm Password : ',validators=[DataRequired(),EqualTo(password)])
    submit=SubmitField('SignUp ',validators=[DataRequired()])
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64))
    password=db.Column(db.String(64))
    score=db.Column(db.Integer)
db.create_all()
l=[]
@app.route('/',methods=['GET','POST'])
def index():
    global l
    logform=loginForm()
    users=Users.query.all()
    if request.method=='POST':
        for i in users:
            if i.username==logform.username.data and i.password==logform.password.data:
                l.append(i.username)
                return redirect(url_for('game'))
        flash('SignUp Please ! ')
        return redirect(url_for('sign'))
    return redirect(url_for('login'))

@app.route('/login',methods=['GET','POST'])
def login():
    logform=loginForm()
    return render_template('login.html',logform=logform)

@app.route('/sign',methods=['GET','POST'])
def sign():
    sform=signForm()
    users=Users.query.all()
    if request.method=='POST':
        for i in users: 
            if i.username==sform.username.data  :
                flash('Already Used')
                return render_template('sign.html',sform=sform)
        u=Users(username=sform.username.data,password=sform.password.data)
        db.session.add(u)
        db.session.commit()
        users=Users.query.all()
    return render_template('sign.html',sform=sform)
@app.route('/game',methods=['GET','POST'])
def game():
    global l
    print(l)
    flash('Welcome')
    flash(l[-1])
    return render_template('game.html')
@app.route('/users',methods=['GET','POST'])
def users():
    U=Users.query.all()
    return render_template('users.html',U=U)

if __name__=='__main__' :
    app.run(debug=True)