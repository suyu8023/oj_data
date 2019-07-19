'''
2019/7/19

'''
from bs4 import BeautifulSoup
import pymysql

class Get_newcoder():

    #牛客网信息
    def parser_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        R_Data = soup.find_all('div', attrs = {'class':"state-num"})
        Rating = R_Data[0].text
        R_Rank = R_Data[1].text
        R_Times = R_Data[2].text
        Times = R_Data[3].text
        if Rating == '暂无':
            Rating = '0'
        if R_Rank == '暂无':
            R_Rank = '0'
        return Rating,R_Rank,R_Times,Times

    # 比赛详情网址
    def detail_competition(self, cid):
        return 'https://ac.nowcoder.com/acm/contest/profile/' + cid


    #存入数据库
    def save_to_mysql(self, cid, rating, rank, times):
        con = pymysql.connect("localhost", "root", "admin", "_info")
        cur = con.cursor()
        sql = 'select * from competition_info where school = "cf", cid = ' + '"' + cid + '"'
        cur.execute(sql)
        cols = cur.fetchall()
        if cols.count() != 0:
            try:
                sql = 'update competition_info set Rating = ' + rating + ', Rank=' + rank +',Times=' + times + 'where shool = newcoder,cid = ' + '"' + cid + '"'
                cur.execute(sql)
                con.commit()
                #判断命令是否成功执行
            except:
                return False
        else:
            sql = "insert into values ('%s','%s','%s','%s','%s')" % ('newcoder', cid, rating, rank, times)
            cur.execute(sql)
            con.commit()
            #判断命令是否成功执行