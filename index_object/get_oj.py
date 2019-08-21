'''
2019/7/19
SDUTOJ数据获取

'''
from bs4 import BeautifulSoup
import pymysql
import time
import re

class Get_oj():

    def parser_html(self, html,cid,difficult_weight,time_weight):
        soup = BeautifulSoup(html, "html.parser")
        c_time = soup.find('span', attrs={'id': "start-time", 'class': "contest-progress-value"}).text
        cid_time = time.mktime(time.strptime(c_time, "%Y-%m-%d %H:%M:%S"))
        for line in soup.tbody.find_all('tr'):
            person_data = line.text.split('\n')
            length = len(person_data)
            nickname = person_data[5].strip('\t')
            for i in range(8,length-1):
                timestamp = person_data[i].strip()# 未提交不记录
                if timestamp != '':
                    time_list = timestamp.split('(')
                    punishment = 0
                    if len(time_list) == 2:
                        punishment = re.search('\d+',time_list[1]).group()
                    problem = chr(i - 8 + ord('A'))
                    self.save_to_mysql(nickname, cid,cid_time,self.change_time(time_list[0]),problem,punishment,difficult_weight,time_weight)

    def change_time(self, timestamp):
        time_list = timestamp.split(":")
        return int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])

    def save_to_mysql(self,nickname,cid,cid_time,pid,ac_time,submissions,difficult_weight,time_weight):
        con = pymysql.connect("localhost", "root", "acm506", "ojdata")
        cur = con.cursor()
        #username,ojclass,cid,cid_time,pid,ac_time,submissions,difficult_weight,time_weight
        sql = "insert into values ('%s','%s','%s','%s','%s','%s','%d','%d','%d')" % (nickname,'oj', cid, cid_time, pid, ac_time, submissions, difficult_weight,time_weight)
        cur.execute(sql)
        con.commit()
        # 判断命令是否成功执行

