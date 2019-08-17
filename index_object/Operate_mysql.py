'''
2019/08/15
'''
import pymysql
import openpyxl

class Operate_mysql():

    # 创建数据表
    # username ,name ,password ,grade ,school ,oj ,vj_account,vj,nc_account,nc,cf_account,cf_count,cf ,rank
    # create table if not exists info(username varchar(15),name varchar(10),password varchar(10),limit int,grade varchar (5),school varchar(10),oj float,vj_account varchar(15),vj float,nc_account varchar(15),nc float,cf_account varchar(15),cf float,rank float)
    # create table if not exists contests(username varchar(15),ojclass varchar(5),cid varchar(10),cid_time TIMESTAMP,pid varchar(5),ac_time varchar(20),submissions int,difficult_weight float,time_weight float)
    # create table if not exists rank_log(username varchar(15),school varchar(10),cid varchar(10),cid_time TIMESTAMP,intergration float)

    # 数据库查询
    def select_public(self, username,name,grade,school):
        user ,nam,gra,sch = '','','',''
        if username != '':
            user = 'username like "%' + username + '%"'
        if name != '':
            nam = 'name like "%' + name + '%"'
        if grade != '':
            gra = 'grade like "%' + grade + '%"'
        if school != '':
            sch = 'school like "%' + school + '%"'
        join_str = ' and '
        join_lis = [user if user != '',nam if nam != '',gra if gra != '',sch if sch != '']
        select_where = join_str.join(join_lis)

        con = pymysql.connect("localhost", "root", "acm506", "ojdata")
        cur = con.cursor()
        sql = 'select school,grade,username,name,oj,vj,nc,cf,rank from info where' + select_where
        cur.execute(sql)
        cols = cur.fetchall()
        con.close()
        return cols

    def select_private(self, username,start_time,end_time):
        con = pymysql.connect("localhost", "root", "acm506", "ojdata")
        cur = con.cursor()
        sql = 'select username,school,cid,intergration from info where username = %s and cid_time > %d and cid_time < %d' % \
              ('"' + username + '"',start_time,end_time)
        cur.execute(sql)
        cols = cur.fetchall()
        con.close()
        if cols.count() != '':
            return True
        else:
            return False

    # 批量添加人员
    def add_persons(self,filename):
        con = pymysql.connect("localhost", "root", "acm506", "ojdata")
        cur = con.cursor()

        wb = openpyxl.load_workbook(filename)
        sheet_names = wb.sheetnames
        sheet = wb[sheet_names[0]]
        for i in range(sheet.max_row):
            username = sheet.cell(row = i+1,column=1).value
            name = sheet.cell(row = i+1, column=2).value
            password = sheet.cell(row = i+1, column=3).value
            grade = sheet.cell(row = i+1, column=4).value
            school = sheet.cell(row = i+1, column=4).value
            sql = "insert into info values ('%s','%s','%s','%s','%s','%f','%s','%f','%s','%f','%s','%f','%f','%d')" % (
                username, name, password, grade, school, 0, '', 0, '', 0, '', 0, 0,1)
            cur.execute(sql)
            con.commit()
        con.close()

    # 添加个人
    def add_person(self,username,name,password,grade,school):
        con = pymysql.connect("localhost", "root", "acm506", "ojdata")
        cur = con.cursor()
        try:
            sql = "insert into info values ('%s','%s','%s','%s','%s','%f','%s','%f','%s','%f','%s','%f','%f','%d')" % (
                username, name, password, grade, school, 0,'',0,'',0,'',0,0,1)
            cur.execute(sql)
            con.commit()
            con.close()
        except:
            return False

    #修改信息
    def update_message(self,username,password,limit):
        con = pymysql.connect("localhost", "root", "acm506", "ojdata")
        cur = con.cursor()
        try:
            if password != '':
                sql = "update info set password = '%s' from info where username = '%s'" % (
                    '"' + password + '"', '"' + username + '"')
                cur.execute(sql)
                con.commit()
            if limit != '':
                sql = "update info set limit = %d from info where username = %s" % (limit,username)
                cur.execute(sql)
                con.commit()
            con.close()
        except:
            return False

    # 登录判断
    def judge_login(self,username, password):
        con = pymysql.connect("localhost", "root", "acm506", "ojdata")
        cur = con.cursor()
        try:
            sql = "select name,limit from info where password = '%s' and username = '%s'" % (
                '"' + password + '"', '"' + username + '"')
            cur.execute(sql)
            cols = cur.fetchall()
            con.close()
            if cols.count() == 0:
                return False
            else:
                return cols[1]
        except:
            return False
