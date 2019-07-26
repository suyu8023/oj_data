'''
2019/7/9
'''
from bs4 import BeautifulSoup
import requests
import random
import json
import time
import re


# def gethtml_json(url):
#     try:
#         user = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
#                 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
#                 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
#                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#                 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#                 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
#                 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
#                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
#                 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
#                 'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
#                 'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
#                 'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
#                 'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
#                 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
#                 'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
#                 'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
#                 'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
#                 'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
#                 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
#                 'UCWEB7.0.2.37/28/999',
#                 'NOKIA5700/ UCWEB7.0.2.37/28/999',
#                 'Openwave/ UCWEB7.0.2.37/28/999',
#                 'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
#                 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
#                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
#                 'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
#                 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
#                 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)',
#                 'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
#                 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
#                 'Mozilla/5.0 (Androdi; Linux armv7l; rv:5.0) Gecko/ Firefox/5.0 fennec/5.0',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
#                 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
#                 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
#                 'Opera/9.80 (Android 2.3.4; Linux; Opera mobi/adr-1107051709; U; zh-cn) Presto/2.8.149 Version/11.10',
#                 'UCWEB7.0.2.37/28/999',
#                 'NOKIA5700/ UCWEB7.0.2.37/28/999',
#                 'Openwave/ UCWEB7.0.2.37/28/999',
#                 'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',]
#         header = {'User Agent': random.choice(user),
#                   'cookie':' _ga=GA1.2.1302475107.1562748137; Jax.Q=17121202036|N3XFSAI76WZ2DRTP4R3726MUA0SQMY; _gid=GA1.2.1872247376.1563782533; JSESSIONID=D01D45CCF756E624F0806C48FAC82E58; _gat=1'}
#         print(url)
#         r = requests.get(url=url, headers=header, timeout=30)
#         r.encoding = 'utf-8'
#         if r.status_code == 200:
#             time.sleep(10)
#             print(r.text + '2')
#             return r.text
#     except:
#         print("False")
#         return None

def judge_problem(problemid, key):
    for i in key:
        if i[0] == problemid:
            return True
    return False

def change_status(status, person_data):
    #找到当前用户
    person = person_data[status[0]]
    #z找到对应题目
    for i in person:
        #更新对应题目
        if i[0] == status[2]:
            #ＡＣ后再次提交
            if i[1] == 'AC':
                break
            else:
                #此次ＡＣ,更新结果，与时间
                if status[2] == 0:
                    i[1] = 'AC'
                    i[-1] = status[3]
                else:
                    i[2] += 1
        #更新个人信息
        person_data[status[0]] = person

def add_new_problem(status, person_data):
    person = person_data[status[0]]
    person.append([status[2],'AC' if status[1]== 0 else 'WA',0 if status[1]== 0 else 1,status[3]])
    person_data[status[0]] = person


def wash_people(person_status):
    person_data = {}
    for key in person_status:
        #首次提交
        if key[0] not in person_data.keys():
            person_data[key[0]] = [[key[2],'AC' if key[1]== 0 else 'WA',0 if key[1]== 0 else 1,key[3]]]
        else:
            problemid = key[2]
            #判断是否提交过，已经提交过
            if judge_problem(problemid, person_data[key[0]]):
                change_status(key,person_data)
            else:
                add_new_problem(key,person_data)
        print(person_data)

def parser_html(text):
    html = json.loads(text)
    if html == None:
        return False
    for i in html.get('submissions'):
        if i[0] == 224173:
            print(i)
    # submissions = html.get("submissions")
    # wash_people(submissions)

if __name__=='__main__':
    with open('te', 'r') as f:
        text = f.read()
        parser_html(text)
    f.close()
    # src = input("比赛id：")
    # urls = ['https://cn.vjudge.net/contest/rank/single/',
    #         'https://vjudge.net/contest/rank/single/']
    # html = gethtml_json(random.choice(urls) + src)
    #parser_html(html)
# 242368
# 242368
#260767



    # cid = html['id']
    #participants = html["participants"]
    #submissions = html["submissions"]
    #person_data = {}
    # #数据清洗
    # for i in submissions:
    #     user = participants[i[0]][0]
    #     print(user)
    #     #判断是否本校人员
    #     solves = {}
    #     problem = chr(i[1] + 1)
    #     print(problem)
    #     result = i[2]
    #     print(result)
    #     timestamp = i[3]
    #     print(timestamp)
    #     if result == 1:
    #         solves[problem] = [result,timestamp,0]
    #     else:
    #         solves[problem] = [result, timestamp, 1]
    #     print(solves)
    #     '''
    #     判断人员是否存在,不存在加入
    #     人员已加入，判断此题是否提交过
    #     提交过，AC过不记录，首次AC记录
    #            WA记录次数（未曾AC），ＡＣ不记录
    #     举例：
    #     {’17121202036‘：{’A‘:[1,381,0(罚时记录)],'B':[0,4558,1]}}
    #     '''
    #     #没有此人提交记录，记录
    #     if user not in  person_data:
    #         person_data[user] = {solves}
    #     else:
    #         solved = person_data[user]    # 获取提交信息
    #         # 此题没有提交过
    #         if problem not in solved.keys():
    #             solved[problem] = solves #更新此题信息
    #             person_data[user] = solved  #更新人员信息
    #         else:#已经提交过
    #             #已ＡＣ
    #             if solved[problem][0] == 1:
    #                 continue
    #             else:
    #                 #首次提交ＡＣ
    #                 if result == 1:
    #                     solved[problem][0] = 1#更新结果
    #                     solved[problem][1] = timestamp#更新时间
    #                     person_data[user] = solved
    #                 else:#再次ＷＡ掉
    #                     solved[problem][2] += 1
    #                     person_data[user] = solved
    #     for j in person_data.keys():
    #         print(person_data[i])