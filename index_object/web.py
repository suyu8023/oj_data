#-*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash
import index_object.reach
import importlib,sys
importlib.reload(sys)

app = Flask(__name__)  # 实例化app对象
app.secret_key = 'sdutacm'

@app.route('/index', methods=['GET','POST'])
def index():
    thead = ['学校','年级','姓名','SDUTOJ','VJ','CF','牛客','总分']
    rank = [
        {
            'school':'SDUT',
            'grade':"信科2017",
            'name':"李雪",
            'SDUTOJ':'531',
            'VJ':'432',
            'CF':'654',
            'NC':'258',
            'SUM':'1875',
            'url':'index/persondata'
        },
        {
            'school':'QNU',
            'grade': "计科2017",
            'name': "李四",
            'SDUTOJ': '521',
            'VJ': '472',
            'CF': '674',
            'NC': '28',
            'SUM':'1695',
            'url':'index/persondata'
        }
    ]
    return render_template('index.html',t_header=thead,t_rank=rank)

@app.route('/')
def person_data():
    return render_template('PersonData.html')

@app.route('/login', methods=['GET','POST'])
def Login():
    Reach = index_object.reach.reseach
    if request.method == 'POST':
        name = request.form.get('user_name')
        pwd = request.form.get('password')
        if not all([name,pwd]):
            flash(u"信息不完整")
        else:
            return render_template('AddNews.html')
    # elif Reach.S_Judge_Admin(name,pwd):
    #     flash("信息有误")

    return render_template('Login.html')

@app.route('/AddNews')
def add_news():
    return render_template('AddNews.html')

if __name__ == '__main__':
    app.run()
