'''
2019/7/19
获取vj比赛数据

'''
from bs4 import BeautifulSoup


class Get_vj():

    def parser_html(self, html):
        cid = html['id']
        #begin = html['begin'] 开始时间
        participants = html['participants']
        submissions = html['submissions']
        person_data = {}
        #数据清洗
        for i in submissions:
            user = participants[i[0]][0]
            #判断是否本校人员
            solves = {}
            problem = char(i[1] + 1)
            result = i[2]
            timestamp = i[3]
            if result == 1:
                solves[problem] = [result,timestamp,0]
            else:
                solves[problem] = [result, timestamp, 1]
            '''
            判断人员是否存在,不存在加入
            人员已加入，判断此题是否提交过
            提交过，AC过不记录，首次AC记录
                   WA记录次数（未曾AC），ＡＣ不记录
            举例：
            {’17121202036‘：{’A‘:[1,381,0(罚时记录)],'B':[0,4558,1]}}
            '''
            #没有此人提交记录，记录
            if user not in  person_data:
                person_data[user] = {solves}
            else:
                solved = person_data[user]    # 获取提交信息
                # 此题没有提交过
                if problem not in solved.keys():
                    solved[problem] = solves #更新此题信息
                    person_data[user] = solved  #更新人员信息
                else:#已经提交过
                    #已ＡＣ
                    if solved[problem][0] == 1:
                        continue
                    else:
                        #首次提交ＡＣ
                        if result == 1:
                            solved[problem][0] = 1#更新结果
                            solved[problem][1] = timestamp#更新时间
                            person_data[user] = solved
                        else:#再次ＷＡ掉
                            solved[problem][2] += 1
                            person_data[user] = solved
