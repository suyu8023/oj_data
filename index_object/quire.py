'''
2019/08/09
数据库查询计算输出
'''
import pymysql

class Quire():
    #单场比赛查询
    def select_contest(self,cid):
        pass
    #姓名查询
    def select_name(self,name):
        pass
    #年纪查询
    def select_grade(self,grade):
        pass
    #时间段查询
    def select_season(self,season):
        pass
    #排序返回
    def select_grade(self,grade,cid,name,season):
        pass
        con = pymysql.connect("localhost", "root", "admin", "_info")
        cur = con.cursor()
        sql = 'select * from competition_info where school = "cf", cid = ' + '"' + cid + '"'
        cur.execute(sql)
        cols = cur.fetchall()
        if cols.count() != 0:
            return False
        else:
            cur.execute(sql)
            con.commit()
            # 判断命令是否成功执行
