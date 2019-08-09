'''
2019/7/19
获取vj比赛数据

'''
from bs4 import BeautifulSoup
import requests
import random
import json

class Get_vj():

    def get_session(self, url,header):
        # 用户登录获取session
        try:
            data = {'username': '17121202036', 'password': '19971302'}
            login_url = url + r'/user/login'
            session = self.requests.session()
            session.post(login_url, data=data, headers=header, timeout=30)
            return session
        except:
            return None

    def judge_problem(self, problemid, key):
        for i in key:
            if i[0] == problemid:
                return True
        return False

    def change_status(self, key, person_data):
        # 找到当前用户
        person = person_data[key[0]]
        # z找到对应题目
        for i in person:
            # 更新对应题目
            if i[0] == key[1]:
                # ＡＣ后再次提交
                if i[1] == 1:
                    break
                else:
                    # AC，修改时间，最后结果
                    if key[2] == 1:
                        i[1] = 1
                        i[-1] = key[-1]
                    else:
                        # WA修改错误次数
                        i[2] += 1

    def add_new_problem(self, key, person_data):
        person = person_data[key[0]]
        person.append([key[1], key[2], 0 if key[2] == 1 else 1, key[3]])
        person_data[key[0]] = person

    def wash_people(self, person_status, limit_time):
        person_data = {}
        # 提交数据
        for key in person_status:
            if key[-1] > limit_time:
                continue
            # 首次提交
            if key[0] not in person_data.keys():
                # 题目序号，提交结果，错误次数，提交时间
                person_data[key[0]] = [[key[1], key[2], 0 if key[2] == 1 else 1, key[3]]]
            else:
                # 用户存在，判断是否提交过该题
                problemid = key[1]
                # 判断是否提交过，已经提交过
                if self.judge_problem(problemid, person_data[key[0]]):
                    self.change_status(key, person_data)
                else:
                    self.add_new_problem(key, person_data)

    def parase_json(self, url, contest_id, session):
        try:
            contest_url = url + r'/contest/rank/single/' + contest_id
            r = session.get(contest_url)
            json_dict = r.text
            html = json.loads(json_dict)
            if html == None:
                return False
            submissions = html.get("submissions")
            limit_time = html.get('length') / 1000
            self.wash_people(submissions, limit_time)
        except:
            return False

    def contestLogin(self,url,contest_id, flag, passwd,header):  # 比赛登陆
        session = self.get_session(url)
        if flag:
            login_url = url + r'/contest/login/' + contest_id
            data = {'password': passwd}
            session.post(login_url, data=data, headers=header)
            self.parase_json(url, contest_id, session=session)
        else:
            self.parase_json(url, contest_id, self.get_session(url))

    def save_to_mysql(self,cid, nickname, solved, time, problem, punishiment):
        pass
