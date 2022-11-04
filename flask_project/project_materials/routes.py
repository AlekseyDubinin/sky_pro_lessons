from app import app, db
from flask import request
from flask import render_template, redirect
from models import Users


@app.route('/', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        a = request.form.to_dict()
        user = Users(name=a['name'], email=a['email'], phone=a['phone'])
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    employees = db.session.query(Users).all()
    print(employees)
    return render_template('index.html', employees=employees)


@app.route('/update', methods=['GET', 'POST'])
def update():
    a = request.form.to_dict()
    user = db.session.query(Users).get(a['id'])

    user.name = a['name']
    user.email = a['email']
    user.phone = a['phone']
    db.session.add(user)
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:id>')
def main(id):
    user = db.session.query(Users).get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/')


