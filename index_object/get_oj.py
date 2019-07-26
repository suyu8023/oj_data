'''
2019/7/19
SDUTOJ数据获取

'''
from bs4 import BeautifulSoup
import pymysql
import time
import re

class Get_oj():

    def parser_html(self, html):
        soup = BeautifulSoup(html, "html.parser")
        time.sleep(10)
        for line in soup.tbody.find_all('tr'):
            person_data = line.text.split('\n')
            length = len(person_data)
            nickname = person_data[5].strip('\t')
            solved = person_data[6]
            for i in range(8,length-1):
                timestamp = person_data[i].strip()# 未提交不记录
                if timestamp != '':
                    time_list = timestamp.split('(')
                    punishment = 0
                    if len(time_list) == 2:
                        punishment = re.search('\d+',time_list[1]).group()
                    problem = chr(i - 8 + ord('A'))
                    self.save_to_mysql(nickname,solved, self.change_time(time_list[0]), problem,punishment)

    def change_time(self, timestamp):
        time_list = timestamp.split(":")
        return int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])

    def save_to_mysql(self,cid, nickname, solved, time, problem, punishiment):
        con = pymysql.connect("localhost", "root", "admin", "_info")
        cur = con.cursor()
        sql = 'select * from competition_info where school = "cf", cid = ' + '"' + cid + '"'
        cur.execute(sql)
        cols = cur.fetchall()
        if cols.count() != 0:
                return False
        else:
            #oj平台,比赛id,nicjname,当前场比赛ＡＣ数量,题目ｉｄ，用时（时间戳），时间权重，难度权重
            sql = "insert into values ('%s',%s','%s','%s','%s','%s','%s','%s','%s')" % ('oj', cid, nickname, solved, time,problem,punishiment,'1.0','1.0')
            cur.execute(sql)
            con.commit()
            # 判断命令是否成功执行

