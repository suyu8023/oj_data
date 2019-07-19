'''
2019/7/19
获取杭电数据

'''

from bs4 import BeautifulSoup
import pymysql
import time
import re

class Get_hdu():

    def change_time(self, timestamp):
        time_list = timestamp.split(":")
        return int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])

    def parser_html(self,cid, html):
        soup = BeautifulSoup(html, "html.parser")
        time.sleep(10)
        index = 0
        length = len(soup.find('tr').find_all('td'))
        person_data = soup.find_all('td')
        C_Data = len(person_data)
        time.sleep(5)
        for line in range(0,C_Data,length):
            index += 1
            if index == 1:
                continue
            name = person_data[line + 1]
            solved = person_data[line + 2]
            print(solved.text)
            for i in range(0, length - 4):
                timestamp = person_data[4 + line].text
                if ":" in timestamp:
                    time_list = timestamp.split('(')
                    punishment = 0
                    if len(time_list) == 2:
                        punishment = re.search('\d+',time_list[1]).group()
                    problem = chr(i + ord('A'))
                    self.save_to_mysql(cid,name,solved, self.change_time(time_list[0]),problem, punishment)

    def save_to_mysql(self, cid, nickname, solved, time, problem, punishiment):
        con = pymysql.connect("localhost", "root", "admin", "_info")
        cur = con.cursor()
        sql = 'select * from competition_info where school = "cf", cid = ' + '"' + cid + '"'
        cur.execute(sql)
        cols = cur.fetchall()
        if cols.count() != 0:
            return False
        else:
            # oj平台,比赛id,nicjname,ＡＣ数量，用时（时间戳）
            sql = "insert into values ('%s',%s','%s','%s','%s','%s','%s')" % ('oj', cid, nickname, solved, time, problem, punishiment, '1')
            cur.execute(sql)
            con.commit()
            # 判断命令是否成功执行

