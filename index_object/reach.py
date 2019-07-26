'''
2019/7/23
'''

import pymysql

class reseach():

    username = set()

    def S_name_cid_school(self, name, cid, school):

        #查找姓名对应的账号
        con = pymysql.connect("localhost", "root", "admin", "person_info")
        cur = con.cursor()
        sql = 'select username from person_info where name = "' + name + '"'
        cur.execute(sql)
        cols = cur.fetchall()
        if cols.count() != 0:
            return False
        else:
            self.username = cols
        con.close()
        #查找账号，对应比赛信息
        con = pymysql.connect("localhost", "root", "admin", "sdut_info")
        cur = con.cursor()
        sql = 'select * from sdut_info where school = "' + school + '", cid = "' + cid + '", username = "' + name + '"'
        cur.execute(sql)
        cols = cur.fetchall()
        if cols.count() != 0:
            return False
        else:
            # oj平台,比赛id,nicjname,ＡＣ数量,题目ｉｄ，用时（时间戳），权重
            sql = "insert into values ('%s',%s','%s','%s','%s','%s','%s')" % (
            'oj', cid, nickname, solved, time, problem, punishiment, '1.0')
            cur.execute(sql)
            con.commit()
            # 判断命令是否成功执行