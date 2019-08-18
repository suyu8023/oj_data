'''
功能：将查询到达的数据格式化成json返回

show_rank：格式首页显示总榜，按username,姓名,年假，学校查询榜单
select_person：格式化个人最近一个月或者规定时间内的比赛情况。个人信息页默认显示最近一个月比赛成绩
select_contests：个人信息，内部显示比赛详情

update: 2019/08/1
'''


class Data_Formatting():

    def show_rank(self,cols):
        # school,grade,username,name,oj,vj,nc,cf,rank
        rank = []
        it = {}
        for item in cols:
            it['school'] = item[0]
            it['grade'] = item[1]
            it['username'] = item[2]
            it['name'] = item[3]
            it['oj'] = item[4]
            it['vj'] = item[5]
            it['nc'] = item[6]
            it['cf'] = item[7]
            it['rank'] = item[8]
            rank.append(it)
        return rank

    def select_person(self,cols):
        # username,school,cid,intergration
        rank = []
        it = {}
        for item in cols:
            it['school'] = item[0]
            it['username'] = item[1]
            it['cid'] = item[2]
            it['intergration'] = item[3]
            rank.append(it)
        return rank

    def select_contests(self,cols):
        #username, ojclass, cid, cid_time, pid, ac_time.submissions, difficult_weight, time_weight
        rank = []
        it = {}
        for item in cols:
            it['username'] = item[0]
            it['ojclass'] = item[1]
            it['cid'] = item[2]
            it['cid_time'] = item[3]
            it['pid'] = item[4]
            it['ac_time'] = item[5]
            it['submissions'] = item[6]
            it['difficult_weight'] = item[7]
            it['time_weight'] = item[8]
            rank.append(it)
        return rank
