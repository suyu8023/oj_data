'''
2019/7/19

'''
from bs4 import BeautifulSoup
import datetime
import pymysql

class Get_newcoder():

    #牛客网信息
    def parser_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        R_Data = soup.find_all('div', attrs = {'class':"state-num"})
        Rating = R_Data[0].text
        if Rating == '暂无':
            Rating = '0'
        return Rating

    # 比赛详情网址
    def detail_competition(self, cid):
        return 'https://ac.nowcoder.com/acm/contest/profile/' + cid

    #存入数据库
    def save_to_mysql(self, account, rating):
        get_time = datetime.datetime.now()
        # account,ojclass, Rating, get_time
        con = pymysql.connect("localhost", "root", "acm506", "ojdata")
        cur = con.cursor()
        sql = "insert into nc_cf values ('%s','%s','%d','%s')" % (account,'newcoder', rating, get_time)
        cur.execute(sql)
        con.commit()
        #判断命令是否成功执
