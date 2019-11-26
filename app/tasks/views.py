from flask import Flask, render_template, flash, url_for,redirect,request, jsonify
from .. import app, db
from models import Task
from forms import createTodo
from datetime import datetime, date, timedelta

db.create_all()

@app.route('/')
def home():
    today = date.today()
    tomorrow = today + timedelta(days=1)
    aftertmr = today + timedelta(days=2)
    tasktoday = Task.query.filter(Task.enddate==today).filter(Task.status==1).order_by(Task.endtime).all()
    tasktmr = Task.query.filter(Task.enddate==tomorrow).filter(Task.status==1).order_by(Task.endtime).all()
    taskoverdue = Task.query.filter(Task.enddate<today).filter(Task.status==1).order_by(Task.endtime).all()
    taskaftertmr = Task.query.filter(Task.enddate>=aftertmr).filter(Task.status==1).order_by(Task.endtime).all()
    return render_template('home.html', taskoverdue= taskoverdue,tasktoday=tasktoday,tasktmr=tasktmr,taskaftertmr=taskaftertmr)

@app.route('/addtodo', methods=['GET', 'POST'])
def addtodo():
    form = createTodo()
    if request.method == 'POST':
        if form.validate_on_submit():
            task = Task(tasktitle = form.tasktitle.data, taskdescription = form.taskdescription.data,enddate = form.enddate.data, endtime=form.endtime.data)
            db.session.add(task)
            db.session.commit()
            flash('Add Tasks Success!','success')
            return redirect(url_for('todolist'))
    return render_template('addtodo.html', form=form)

@app.route('/tasktoday')
def tasktoday():
    todo = date.today()
    tasktodo = Task.query.filter(Task.enddate==todo).order_by(Task.endtime).all()
    return render_template('today.html',tasktodo=tasktodo)

@app.route('/drafttodo')
def drafttodo():
    tasktodo = Task.query.filter(Task.enddate== None).filter(Task.status==1).order_by(Task.createdate).all()
    return render_template('drafttodo.html',tasktodo=tasktodo)


@app.route('/todo', methods=['GET', 'POST'])
def todolist():
    if request.method == 'POST':
        taskid = request.form.get('btnId')
        task = Task.query.get(taskid)
        return render_template('todo.html',task=task)
    else:
        return redirect(url_for('home'))

@app.route('/tododone', methods=['GET', 'POST'])
def tododone():
    if request.method == 'POST':
        taskid = request.form.get('btnAcheive')
        task = Task.query.get(taskid)
        task.status = 0
        db.session.commit()
        flash('Yeah you have done your task. Congrat!','success')
        return redirect(url_for('tasktoday'))
    else:
        return redirect(url_for('home'))

@app.route('/todoedit', methods=['GET', 'POST'])
def todoedit():
    forms=createTodo()
    if request.method == 'POST':
        taskid = request.form.get('btnEdit')
        task = Task.query.get(taskid)
        print task.taskdescription
        return render_template('todoedit.html',forms=forms,task=task)
    else:
        return redirect(url_for('home'))

@app.route('/todoupdate', methods=['GET', 'POST'])
def todoupdate():
    if request.method == 'POST':
        taskid = request.form.get('btnUpdate')
        task = Task.query.get(taskid)
        task.tasktitle = request.form.get('tasktitle')
        task.taskdescription = request.form.get('taskdescription')
        task.enddate = request.form.get('enddate')
        task.endtime = request.form.get('endtime')
        db.session.commit()
        flash('Your task is edited!','success')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))

@app.route('/tododel', methods=['GET', 'POST'])
def tododel():
    if request.method == 'POST':
        taskid = request.form.get('btnDelete')
        task = Task.query.get(taskid)
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('viewtododone'))
    else:
        return redirect(url_for('viewtododone'))

@app.route('/viewtododone')
def viewtododone():
    task = Task.query.filter(Task.status==0).filter(Task.enddate!=None).filter(Task.endtime!=None).order_by(Task.enddate.desc()).all()
    taskdraft = Task.query.filter(Task.status==0).filter(Task.enddate==None).filter(Task.endtime==None).order_by(Task.enddate.desc()).all()
    return render_template('tododone.html', task= task, taskdraft=taskdraft)

@app.route('/toredo', methods=['GET', 'POST'])
def toredo():
    if request.method == 'POST':
        taskid = request.form.get('btnAcheive')
        task = Task.query.get(taskid)
        task.status = 1
        db.session.commit()
        flash('You may miss some parts, so let do it again!','warning')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


