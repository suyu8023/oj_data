#-*- coding:utf-8 -*-
import json
from flask import Flask, render_template

app = Flask(__name__)  # 实例化app对象

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
