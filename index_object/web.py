#-*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash
from index_object.Operate_mysql import Operate_mysql
from index_object.get_data import crawl_data
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
    return render_template('index.html',t_header=thead,t_rank=rank, Login=login)

@app.route('/index/persondata',methods=['GET','POST'])
def Person_data():
    #username,school,cid,intergration
    if request.method == 'get':
        start_time = request.get('start_time')
        end_time = request.get('end_time')
        username = request.get('username')
        thead = ['username','oj平台','比赛id','积分']
        oj_data = Operate_mysql.select_person(username,start_time,end_time)
        back = '/index'
    return render_template('Persondata.html',t_header=thead,oj=oj_data,back_url=back)

@app.route('/index/login', methods=['GET','POST'])
def Login():
    if request.method == 'POST':
        name = request.form.get('user_name')
        pwd = request.form.get('password')
        result = Operate_mysql.judge_login(username=name, password=pwd)
        if result == 'admin':
            return render_template('Admin.html')
        elif result == 'teacher':
            return render_template('Teacher.html')
        elif result == 'student':
            return render_template('Student.html')
        else:
            return render_template('Login.html')

    return render_template('Login.html')

@app.route('/index/student', methods=['POST','GET'])
def Student():
    if request.method == 'POST':
        username = request.form.get('username')
        cid = request.form.get('cid')
        ojclass = request.form.get('ojclass')
        username1 = request.form.get('username1')
        username2 = request.form.get('username2')
        username3 = request.form.get('username3')
        result = Operate_mysql.results_dubbing(username, cid, ojclass, username1, username2, username3)
        if result:
            return flash('成功添加！！！')
    return flash('添加失败！！！')

@app.route('/index/teacher', methods=['GET','POST'])
def Teacher():
    if request.method == 'POST':
        ojclass = request.form.get('ojclass')
        cid = request.form.get('cid')
        difficult_weight = request.form.get('difficult')
        time_weight = request.form.get('time')
        if crawl_data.getdata_json(cid,ojclass):
            pass

@app.route('/Admin',methods=['GET','POST'])
def Admin():
    if request.method == 'POST':
        # 修改密码
        username = request.form.get('username')
        pwd = request.form.get('password')
        #修改权限
        username = request.form.get('username')
        #username,name,password,grade,school
        username = request.form.get('username')
        pwd = request.form.get('password')
        grade = request.form.get('grade')
        school = request.form.get('grade')
    return render_template('Admin.html')

if __name__ == '__main__':
    app.run()
