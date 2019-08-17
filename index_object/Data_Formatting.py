'''
2019/08/15
    将查询到的数据  json  化
2019/08/17
    更新续写
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

    def select_private(self,cols):
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
