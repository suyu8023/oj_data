'''
2019/7/19
获取ｃｆ数据

'''

from bs4 import BeautifulSoup
import pymysql
import time

class Get_oj():

    #获取比赛ｒａｔｉｎｇ
    def parser_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(15)
        rating_data = soup.find('table', attrs={'class': 'tablesorter user-contests-table'}).tbody.find('tr')
        if rating_data == False
            return False
        else:
            Rating = rating_data.find_all('td')
            R_Rating = Rating[5].text
            R_Rank = Rating[2].text
            R_Times = Rating[0].text
            return R_Rating,R_Rank,R_Times

    #比赛详情网址
    def detail_competition(self, cid):
            return 'http://codeforces.com/contests/with/' + cid

    #存入数据库
    def save_to_mysql(self, cid, rating, rank, times):
        con = pymysql.connect("localhost", "root", "admin", "comprtition_info")
        cur = con.cursor()
        sql = 'select * from competition_info where school = "cf", cid = "' + cid + '"'
        cur.execute(sql)
        cols = cur.fetchall()
        if cols.count() != 0:
            try:
                sql = 'update competition_info set Rating = ' + rating + ', Rank=' + rank +',Times=' + times + 'where shool = cf,cid = ' + '"' + cid + '"'
                cur.execute(sql)
                con.commit()
                #判断命令是否成功执行
            except:
                return False
        else:
            sql = "insert into values ('%s','%s','%s','%s','%s')" % ('cf', cid, rating, rank, times)
            cur.execute(sql)
            con.commit()
            #判断命令是否成功执行
