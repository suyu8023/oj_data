#-*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from index_object.Operate_mysql import Operate_mysql
import importlib,sys
importlib.reload(sys)

app = Flask(__name__)
app.secret_key = 'sdutacm'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:acm506@127.0.0.1/ojdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=['GET','POST'])
def index():
    thead = ['学校','年级','姓名','SDUTOJ','VJ','CF','牛客','总分']
    rank = query(Operate_mysql.create_consumer).order_by()
    login = '/index/login'
    return render_template('index.html',t_header=thead,t_rank=rank,Login=login)

@app.route('/index/persondata')
def Person_data():
    #提交平台,比赛id,nickname,当前场比赛ＡＣ数量,题目ｉｄ，用时（时间戳），时间权重，难度权重
    thead = ['提交平台','比赛id','nickname','姓名','AC','本场积分']
    oj_data=[
        {
            'school':'oj',
            'cid':'2726',
            'nickname':'17121202036',
            'name':'李雪',
            'solved':'6',
            'sum':'52'
        },
        {
            'school': 'oj',
            'cid': '27206',
            'nickname': '17121202036',
            'name':'李四',
            'solved': '4',
            'sum': '36'
        }
    ]
    vj_data=[
        {
            'school': 'vj',
            'cid': '2736',
            'nickname': '17121202036',
            'name':'赵四',
            'solved': '2',
            'sum': '32'
        },
        {
            'school': 'vj',
            'cid': '2456',
            'nickname': '17121202036',
            'name':'尼古拉斯·赵四',
            'solved': '1',
            'sum': '6'
        }
    ]
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
