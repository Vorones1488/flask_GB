from flask import Flask, request, render_template, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash
from models import Register, Student, db
from flask_wtf.csrf import CSRFProtect
from forms import LoginForm
from random import randint

app = Flask(__name__)
# app.secret_key = b'd962ea0e739a57e13f523ac4c0d843d2ecde7120cf6722cf4a13811d5cb10d3e'

app.config['SECRET_KEY'] = b'd962ea0e739a57e13f523ac4c0d843d2ecde7120cf6722cf4a13811d5cb10d3e'

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///mydatabase.db'
db.init_app(app)

csrf = CSRFProtect(app)

@app.cli.command("init_db")
def init_db():
    db.create_all()
    print('База данных создана')


@app.route('/', methods=['GET', 'POST'])
def index():
    form_register = LoginForm()
    try:
        if request.method == 'POST' and form_register.validate():
            user_name = form_register.username.data
            email = form_register.email.data
            password_hash = generate_password_hash(form_register.password.data)
            register_user = Register(username=user_name, email=email, password=password_hash)
            db.session.add(register_user)
            db.session.commit()
            return redirect(url_for('db_viv', usernames=user_name))
    except: 
        db.session.rollback()
        print("пользователь или почта не уникальны")
    return render_template('index.html', form=form_register)
        


@app.route('/redirect/<usernames>',)
def db_viv(usernames):
    register_user = Register.query.filter_by(username=usernames).first()
    student = Student(name='Миша', firstname='Гарилов', group='L-102', userid=register_user.id)
    db.session.add(student)
    db.session.commit()
    res = db.session.query(Register, Student).join(Student, Register.id == Student.userid).all()
    if res:
        
        return jsonify([{'user_name': result.Register.username, 'Name': result.Student.name, "e-mail": result.Register.email, 'great': result.Student.shool_asses} for result in res])
    else:
        return f'почему то ничего нет странно'

@app.cli.command("create_user")
def clic(names='vbn'):
    for i in range(1, 10):
        password = '12345678{i}'
        password_hash = generate_password_hash(password)
        register_user = Register(username=f'user{i}', email=f"email{i}@mail.ru", password=password_hash)
        db.session.add(register_user)
        db.session.flush()
        student = Student(name=f'name{i}', firstname=f'family{i}', group=f'L-10{i}', userid=register_user.id, shool_asses=randint(2, 5))
        db.session.add(student)
    db.session.commit()
    
    





        
    

