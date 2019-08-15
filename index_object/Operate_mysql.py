'''
2019/08/15
'''
from flask_sqlalchemy import SQLAlchemy

class Operate_mysql():

    # 创建数据表
    def create_consumer(self, db):
        __tablename__ = 'consumers'
        username = db.Column(db.String(16),primary_key=True)
        name = db.Column(db.String(10))
        password = db.Column(db.String(10))
        grade = db.Column(db.String(10))
        school = db.Column(db.String(10))
        oj = db.Column(db.Float)
        vj = db.Column(db.Float)
        nc = db.Column(db.Float)
        cf = db.Column(db.Float)
        rank = db.Column(db.Float)

    def create_contests(self, db):
        __tablename__ = 'contests'
        id = db.Model(db.INTEGER, primary_key=True)
        # 用户名，比赛平台，比赛id，比赛时间，题目序号，题目提交时间，错误次数，难度权重，时间权重
        username = db.Column(db.String(16), db.ForeignKey('rank_log.cid'))
        school = db.Column(db.String(10))
        cid = db.Column(db.INTEGER)
        cid_time = db.Column(db.String(20))
        pid = db.Column(db.String(3))
        ac_time = db.Column(db.String(10))
        submissions = db.Column(db.INTEGER)
        difficult_weight = db.Column(db.Float)
        time_weight = db.Column(db.Float)

    def create_rank(self,db):
        __tablename__ = 'rank_log'
        id = db.Model(db.INTEGER, primary_key=True)
        username = db.Column(db.String(16))
        school = db.Column(db.String(10))
        # 关系引用
        cid = db.relationship('self.create_contests', backref='employer')
        cid_time = db.Column(db.String(20))
        intergration = db.Column(db.Float)

    # 数据库查询
    def select_username(self, username):
        pass

    def select_name(self, name):
        pass

    def select_grade(self, grade):
        pass

    def select_time(self, start_time,end_time):
        pass

    # 人员添加
    def add_persons(self,filename):
        pass

    def add_person(self,db,username,name,password,grade,school):
        user = self.create_consumer(username=username,name=name,password=password,grade=grade,school=school,oj=0,vj=0,nc=0,cf=0,rank=0)
        db.sessionn.add(user)
        db.sessionn.commit()
        pass

    #修改信息
    def update_message(self,username,password):
        pass

    # 登录判断
    def judge_login(self,username, password):
        pass
