#-*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from index_object.Operate_mysql import Operate_mysql
import importlib,sys
importlib.reload(sys)

app = Flask(__name__)
app.secret_key = 'sdutacm'


@app.route('/', methods=['GET','POST'])
def index():
    # school,grade,username,name,oj,vj,nc,cf,rank
    thead = ['学校','年级','username','姓名','SDUTOJ','VJ','CF','牛客','总分']
    rank = Operate_mysql.show_rank()
    login = '/index/login'
    return render_template('index.html',t_header=thead,t_rank=rank,Login=login)

@app.route('/index/persondata')
def Person_data():
    #username,school,cid,intergration
    thead = ['username','oj平台','比赛id','积分']
    oj_data =
    return render_template('Persondata.html',t_header=thead,oj=oj_data,vj=vj_data)

@app.route('/index/login', methods=['GET','POST'])
def Login():
    Reach = index_object.reach.reseach
    if request.method == 'POST':
        name = request.form.get('user_name')
        pwd = request.form.get('password')
        if not all([name,pwd]):
            flash(u"信息不完整")
        else:
            return render_template('Admin.html')
    # elif Reach.S_Judge_Admin(name,pwd):
    #     flash("信息有误")

    return render_template('Login.html')

@app.route('/Admin',methods=['GET','POST'])
def Admin():
    if request.method == 'POST':
        username = request.form.get('username')
        name = request.form.get('name')
        pwd = request.form.get('password')
        school = request.form.get('school')
        grade = request.form.get('grade')
        if not all([username,name,pwd,school,grade]):
            flash("信息不完整",'error')
        else:
            flash('成功导入')
    pid = ['A','B','C']
    return render_template('Admin.html',pids=pid)

if __name__ == '__main__':
    db.drop_all() #删除表
    db.create_all()
    app.run()
