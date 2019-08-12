#-*- coding:utf-8 -*-

from flask import Flask, render_template,request

app = Flask(__name__)  # 实例化app对象

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Login', methods=['get','post'])
def Login():
    return render_template('Login.html')

if __name__ == '__main__':
    app.run()
