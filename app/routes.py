# -*- coding: utf-8 -*-
from flask import render_template,flash,redirect,url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'username':'Странник'}
    posts= [
        {
        'author': {'username': 'Alexander'},
        'body':'Beautiful day in Novosibirsk!'
        },
        {
        'author': {'username': 'Ксения'},
        'body': 'Мстители - клевый фильм'
        },
        {
        'author': {'username': 'Ипполит'},
        'body': 'Обожаю пивко'
        }
    ]
    return render_template('index.html', title='Домашняя',user=user, posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():

        flash('Login requested for user {}, password={} remember_me={}'.format(form.username.data, form.password.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign in', form=form)