# -*- coding: utf-8 -*-
from flask import render_template
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

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title='Авторизация', form=form)