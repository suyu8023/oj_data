'''
2019/08/08

'''

import requests
import random
import json


def get_header():
    user = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
            'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
            'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
            'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
            'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
            'UCWEB7.0.2.37/28/999',
            'NOKIA5700/ UCWEB7.0.2.37/28/999',
            'Openwave/ UCWEB7.0.2.37/28/999',
            'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; .NET CLR 2.0.50727)',
            'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Androdi; Linux armv7l; rv:5.0) Gecko/ Firefox/5.0 fennec/5.0',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            'Opera/9.80 (Android 2.3.4; Linux; Opera mobi/adr-1107051709; U; zh-cn) Presto/2.8.149 Version/11.10',
            'UCWEB7.0.2.37/28/999',
            'NOKIA5700/ UCWEB7.0.2.37/28/999',
            'Openwave/ UCWEB7.0.2.37/28/999',
            'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999', ]
    return {'User Agent': random.choice(user)}

def get_session(url):
    # 用户登录获取session
    try:
        data = {'username': '17121202036', 'password': '19971302'}
        login_url = url + r'/user/login'
        session = requests.session()
        session.post(login_url, data=data, headers=get_header(), timeout=30)
        return session
    except:
        return None

def judge_problem(problemid, key):
    for i in key:
        if i[0] == problemid:
            return True
    return False

def change_status(key, person_data):
    #找到当前用户
    person = person_data[key[0]]
    #z找到对应题目
    for i in person:
        #更新对应题目
        if i[0] == key[1]:
            #ＡＣ后再次提交
            if i[1] == 1:
                break
            else:
                #AC，修改时间，最后结果
                if key[2] == 1:
                    i[1] = 1
                    i[-1] = key[-1]
                else:
                    # WA修改错误次数
                    i[2] += 1

def add_new_problem(key, person_data):
    person = person_data[key[0]]
    person.append([key[1],key[2],0 if key[2]==1 else 1,key[3]])
    person_data[key[0]] = person

def wash_people(html,difficult_weight, time_weight):
    # username,ojclass,cid,cid_time,pid,ac_time,submissions,difficult_weight,time_weight
    cid = html.get('id')
    cid_time = html.get('begin') / 1000
    person_status = html.get("submissions")
    participants = html.get('participants')
    limit_time = html.get('length') / 1000

    person_data = {}
    # 提交数据
    for key in person_status:
        if key[-1] > limit_time:
            continue
        #首次提交
        if key[0] not in person_data.keys():
            # 题目序号，提交结果，错误次数，提交时间
            person_data[key[0]] = [[key[1],key[2],0 if key[2]==1 else 1,key[3]]]
        else:
            # 用户存在，判断是否提交过该题
            problemid = key[1]
            #判断是否提交过，已经提交过
            if judge_problem(problemid, person_data[key[0]]):
                change_status(key,person_data)
            else:
                add_new_problem(key,person_data)
    print(person_data)
    for key in person_data.keys():
        # username,ojclass,cid,cid_time,pid,ac_time,submissions,difficult_weight,time_weight
        username = participants[str(key)][0]
        print(username)
        problem = person_data[key]
        for it in problem:
            pid = chr(it[0] + ord('A'))
            ac_time = it[3] + cid_time
            submissions = it[2]
            if it[1] == 1:
                print(username,cid,cid_time,pid,ac_time,submissions)



def parase_json(url, contest_id, session):
    try:
        contest_url = url + r'/contest/rank/single/' + contest_id
        r = session.get(contest_url)
        json_dict = r.text
        html = json.loads(json_dict)
        if html == None:
            return False
        submissions = html.get("submissions")
        participants = html.get('participants')
        limit_time = html.get('length') / 1000
        wash_people(html, submissions, limit_time)
    except:
        return False

def contestLogin(contest_id,flag, passwd):  # 比赛登陆
    try:
        url = 'https://cn.vjudge.net'
    except:
        url = 'https://vjudge.net'
    session = get_session(url)
    if flag:
        login_url = url + r'/contest/login/' + contest_id
        data = {'password': passwd}
        session.post(login_url, data=data, headers=get_header())
        parase_json(url, contest_id, session=session)
    else:
        parase_json(url, contest_id, get_session(url))

if __name__=='__main__':
    #passwd = input('密码')
    contest_id = '249792'
    contestLogin(contest_id,True,'gongbutangjuan')
