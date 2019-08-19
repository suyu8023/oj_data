'''
2019/7/19
获取ｃｆ数据

'''

from bs4 import BeautifulSoup
import datetime
import pymysql
import time

class Get_oj():
# # account,ojclass, Rating, R_Rank, R_Times, S_Times, get_time
    #获取比赛ｒａｔｉｎｇ
    def parser_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(15)
        rating_data = soup.find('table', attrs={'class': 'tablesorter user-contests-table'}).tbody.find('tr')
        if rating_data == False:
            return False
        else:
            Rating = rating_data.find_all('td')
            Rating = Rating[5].text
            return Rating

    #比赛详情网址
    def detail_competition(self, cid):
            return 'http://codeforces.com/contests/with/' + cid

    #存入数据库
    def save_to_mysql(self, rating, account):

        get_time = datetime.datetime.now()
        # account,ojclass, Rating,get_time
        con = pymysql.connect("localhost", "root", "acm506", "ojdata")
        cur = con.cursor()
        sql = "insert into nc_cf values ('%s','%s','%d','%s')" % (account, 'cf', rating, get_time)
        cur.execute(sql)
        con.commit()
        #判断命令是否成功执行
