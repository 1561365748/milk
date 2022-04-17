import pymysql
import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render
from .models import User
from math import sqrt
import operator
from django.http import HttpResponseRedirect
calsum=0
pastuser=""
# 2.1 构造物品-->物品的共现矩阵
# 2.2 计算物品与物品的相似矩阵
result={}
def similarity(data):
    # 2.1 构造物品：物品的共现矩阵
    N = {}  # 喜欢物品i的总人数
    C = {}  # 喜欢物品i也喜欢物品j的人数
    for user, item in data.items():
        uid = user
        result.setdefault(uid, {})
        for i, score in item.items():
            N.setdefault(i, 0)
            N[i] += 1
            C.setdefault(i, {})

            for j, scores in item.items():
                if j not in i:
                    C[i].setdefault(j, 0)
                    C[i][j] += 1

    # 2.2 计算物品与物品的相似矩阵
    W = {}
    for i, item in C.items():
        W.setdefault(i, {})
        for j, item2 in item.items():
            W[i].setdefault(j, 0)
            W[i][j] = C[i][j] / sqrt(N[i] * N[j])

    return W

# 3.根据用户的历史记录，给用户推荐物品
def recommandList(data, W, user, k=5, N=10):
    rank = {}
    for i, score in data[user].items():  # 获得用户user历史记录，如A用户的历史记录为{'a': '1', 'b': '1', 'd': '1'}
        for j, w in sorted(W[i].items(), key=operator.itemgetter(1), reverse=True)[0:k]:  # 获得与物品i相似的k个物品
            if j not in data[user].keys():  # 该相似的物品不在用户user的记录里
                rank.setdefault(j, 0)
                rank[j] += float(score) * w
                result[user][j] = rank[j]
            else:
                result[user][j] = 0
    #print("为用户", user, "推荐----")
    #print(sorted(rank.items(), key=operator.itemgetter(1), reverse=True)[0:N])
    return sorted(rank.items(), key=operator.itemgetter(1), reverse=True)[0:N]

def cal(request):
    global calsum
    global result
    global pastuser
    if request.method=='GET':
        calsum=0
        big_sum = 458.5
        mid_sum = 327.5
        big_rest = round(big_sum - 270, 2)
        mid_rest = round(mid_sum - 270, 2)

        alltip = "您可通过以下方式消耗过剩的的卡路里："
        bsport1 = round(big_rest/900, 1)
        bsport2 = round(big_rest/600, 1)
        bsport3 = round(big_rest/700, 1)
        bsport4 = round(big_rest/400, 1)
        bsport5 = round(big_rest/650, 1)
        bsport6 = round(big_rest/700, 1)
        bsport7 = round(big_rest/450, 1)
        bsport8 = round(big_rest/400, 1)

        msport1 = round(mid_rest/900, 1)
        msport2 = round(mid_rest/600, 1)
        msport3 = round(mid_rest/700, 1)
        msport4 = round(mid_rest/400, 1)
        msport5 = round(mid_rest/650, 1)
        msport6 = round(mid_rest/700, 1)
        msport7 = round(mid_rest/450, 1)
        msport8 = round(mid_rest/400, 1)
        return render(request, 'calorie.html', locals())

    elif request.method=='POST':
        if request.POST['ingredients_quantity']==''and request.POST['username']=='':
            message="请输入小料及数量或用户名"
            calsum = 0
            big_sum = 458.5
            mid_sum = 327.5
            big_rest = round(big_sum - 270, 2)
            mid_rest = round(mid_sum - 270, 2)

            alltip = "您可通过以下方式消耗过剩的卡路里："
            bsport1 = round(big_rest / 900, 1)
            bsport2 = round(big_rest / 600, 1)
            bsport3 = round(big_rest / 700, 1)
            bsport4 = round(big_rest / 400, 1)
            bsport5 = round(big_rest / 650, 1)
            bsport6 = round(big_rest / 700, 1)
            bsport7 = round(big_rest / 450, 1)
            bsport8 = round(big_rest / 400, 1)

            msport1 = round(mid_rest / 900, 1)
            msport2 = round(mid_rest / 600, 1)
            msport3 = round(mid_rest / 700, 1)
            msport4 = round(mid_rest / 400, 1)
            msport5 = round(mid_rest / 650, 1)
            msport6 = round(mid_rest / 700, 1)
            msport7 = round(mid_rest / 450, 1)
            msport8 = round(mid_rest / 400, 1)

            return render(request, 'calorie.html', locals())

        elif request.POST['ingredients_quantity']=='' and request.POST['ingredients_choice']=='':
            like = "猜您喜欢"
            like1=""
            if(request.POST['username']!='0201120001' and request.POST['username']!='0201120002' and request.POST['username']!='0201120003'):
                like = "您尚未使用过本网页，先看看其他用户的喜好吧"
                nowuser ='0201120001'
            else:
                nowuser = request.POST['username']
                like1 = "图 中 为 您 定 制 的 最 佳 五 种 配 料"
            #算法---————————樊蕾靓
            # 创建连接
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                                   db='milk', charset='utf8')
            # 创建游标
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 创建二维数组 data[user][item]
            sql = "select user,芋圆, 奥利奥,椰果,红豆,仙草,椰子冻,奶盖,西米,珍珠,布丁 from user_item"
            cursor.execute(sql)
            temdata = cursor.fetchall()
            # temdata = [u][v]
            # 关闭游标
            conn.close()
            # 关闭连接
            cursor.close()

            # 算法---————————袁磊
            data = {}
            for i in temdata:
                for key in i:
                    data.setdefault(i[key], {})
                    tem = i[key]
                    break
                for key in i:
                    if key != 'user':
                        if i[key] != 0:
                            data[tem].update({key: i[key]})
            W = similarity(data)  # 计算物品相似矩阵
            recommandList(data, W, nowuser, 10, 10)  # 推荐

            list = []
            list = sorted(result[nowuser].items(), key=operator.itemgetter(1), reverse=True)[0:5]

            # 算法---————————赵霖
            #降序
            list = sorted(list, key=lambda x: x[1],reverse=False)[0:5]

            #清空数据表
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='milk', charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            sql = "TRUNCATE user"
            cursor.execute(sql)
            cursor.close()
            conn.close()

            #存入数据
            for i in list:
                db = User()
                db.user = nowuser
                db.ingredient =i[0]
                db.num =i[1]
                db.save()


            #for i in result:
            #    for j in result[i]:
            #            db = User()
            #            db.user =i
            #            db.ingredient=j
            #            db.num =result[i][j]
            #            db.save()

            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='milk', charset='utf8')
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            if nowuser == '0201120002':
                cursor.execute("select user,ingredient from user where user='0201120002' ")
                ingredient = [item['ingredient'] for item in cursor.fetchall()]
                cursor.execute("select user,num from user where user='0201120002'")
                num = [item['num'] for item in cursor.fetchall()]
            elif nowuser == '0201120003':
                cursor.execute("select user,ingredient from user where user='0201120003'")
                ingredient = [item['ingredient'] for item in cursor.fetchall()]
                cursor.execute("select user,num from user where user='0201120003'")
                num = [item['num'] for item in cursor.fetchall()]
            elif nowuser == '0201120001':
                cursor.execute("select user,ingredient from user where user='0201120001'")
                ingredient = [item['ingredient'] for item in cursor.fetchall()]
                cursor.execute("select user,num from user where user='0201120001'")
                num = [item['num'] for item in cursor.fetchall()]
            cursor.close()
            conn.close()
            # 显示中文
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False
            # 修改图的大小
            plt.figure(dpi=110)
            # y轴转化为np类型数组
            y = np.asarray(num)
            plt.barh(ingredient, y,color='grey')  # 横放条形图函数 barh
            plt.title('推荐小料')
            #plt.show()
            plt.savefig("./static/img/rec.jpg")

            calsum = 0
            big_sum = 458.5
            mid_sum = 327.5
            big_rest = round(big_sum - 270, 2)
            mid_rest = round(mid_sum - 270, 2)

            alltip = "您可通过以下方式消耗过剩的卡路里："
            bsport1 = round(big_rest / 900, 1)
            bsport2 = round(big_rest / 600, 1)
            bsport3 = round(big_rest / 700, 1)
            bsport4 = round(big_rest / 400, 1)
            bsport5 = round(big_rest / 650, 1)
            bsport6 = round(big_rest / 700, 1)
            bsport7 = round(big_rest / 450, 1)
            bsport8 = round(big_rest / 400, 1)

            msport1 = round(mid_rest / 900, 1)
            msport2 = round(mid_rest / 600, 1)
            msport3 = round(mid_rest / 700, 1)
            msport4 = round(mid_rest / 400, 1)
            msport5 = round(mid_rest / 650, 1)
            msport6 = round(mid_rest / 700, 1)
            msport7 = round(mid_rest / 450, 1)
            msport8 = round(mid_rest / 400, 1)

            return render(request, 'recommend.html', locals())

        elif request.POST['ingredients_quantity']!='':
            nowuser = request.POST['username']
            name=request.POST['ingredients_choice']
            num=float(request.POST['ingredients_quantity'])
            if(pastuser==""):
                pastuser=nowuser
            if(pastuser==nowuser):
                mid_sum=0
                big_sum=0
                sum=0
                calsum=0
                if name=='芋圆':
                    calsum+=(num/100)*135
                elif name=='奥利奥':
                    calsum += (num / 100) * 490
                elif name == '椰果':
                    calsum += (num / 100) * 241
                elif name == '红豆':
                    calsum += (num / 100) * 224
                elif name == '仙草':
                    calsum += (num / 100) * 61
                elif name == '椰子冻':
                    calsum += (num / 100) * 330
                elif name == '奶盖':
                    calsum += (num / 100) * 390
                elif name == '西米':
                    calsum += (num / 100) * 358
                elif name == '珍珠':
                    calsum += (num / 100) * 81
                elif name == '布丁':
                    calsum += (num / 100) * 174
                elif name == '花生麻薯':
                    calsum += (num / 100) * 203
                elif name == '寒天':
                    calsum += (num / 100) * 42
                elif name == '燕麦':
                    calsum += (num / 100) * 367
                elif name == '咖啡冻':
                    calsum += (num / 100) * 56
                elif name == '芋泥':
                    calsum += (num / 100) * 171
                elif name == '芝麻芋圆':
                    calsum += (num / 100) * 37
                elif name == '抹茶芋圆':
                    calsum += (num / 100) * 110
                elif name == '布蕾':
                    calsum += (num / 100) * 251
                elif name == '茶冻':
                    calsum += (num / 100) * 38
                elif name == '熟糯米':
                    calsum += (num / 100) * 348
                elif name == '薏仁':
                    calsum += (num / 100) * 361
                sum+=calsum
                big_sum= round(sum+458.5,2)
                mid_sum=round(sum+327.5,2)
                big_rest=round(big_sum-270,2)
                mid_rest=round(mid_sum-270,2)

                alltip="您可通过以下方式消耗过剩的卡路里："
                bsport1 = round(big_rest / 900, 1)
                bsport2 = round(big_rest / 600, 1)
                bsport3 = round(big_rest / 700, 1)
                bsport4 = round(big_rest / 400, 1)
                bsport5 = round(big_rest / 650, 1)
                bsport6 = round(big_rest / 700, 1)
                bsport7 = round(big_rest / 450, 1)
                bsport8 = round(big_rest / 400, 1)

                msport1 = round(mid_rest / 900, 1)
                msport2 = round(mid_rest / 600, 1)
                msport3 = round(mid_rest / 700, 1)
                msport4 = round(mid_rest / 400, 1)
                msport5 = round(mid_rest / 650, 1)
                msport6 = round(mid_rest / 700, 1)
                msport7 = round(mid_rest / 450, 1)
                msport8 = round(mid_rest / 400, 1)

                # 获取calculate.html中的输入值(包括用户值，小料的名称，数量值)
                u = request.POST.get('username')
                v = request.POST.get('ingredients_choice')
                d = request.POST.get('ingredients_quantity')
                # 创建连接
                conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                                       db='milk', charset='utf8')
                # 创建游标
                cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

                # 执行SQL
                cursor.execute("update paint set sum=sum+1 where ingredients_choice=%s", [v])
                conn.commit()

                # 关闭游标
                conn.close()
                # 关闭连接
                cursor.close()

                # 创建连接
                conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                                       db='milk', charset='utf8')
                # 创建游标
                cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

                #算法————————樊蕾靓
                # 执行SQL
                if v == '芋圆':
                    cursor.execute("update user_item set 芋圆=芋圆+1 where user=%s ", [u])
                elif v == '奥利奥':
                    cursor.execute("update user_item set 奥利奥=奥利奥+1 where user=%s ", [u])
                elif v == '椰果':
                    cursor.execute("update user_item set 椰果=椰果+1 where user=%s ", [u])
                elif v == '红豆':
                    cursor.execute("update user_item set 红豆=红豆+1 where user=%s ", [u])
                elif v == '仙草':
                    cursor.execute("update user_item set 仙草=仙草+1 where user=%s ", [u])
                elif v == '椰子冻':
                    cursor.execute("update user_item set 椰子冻=椰子冻+1 where user=%s ", [u])
                elif v == '奶盖':
                    cursor.execute("update user_item set 奶盖=奶盖+1 where user=%s ", [u])
                elif v == '西米':
                    cursor.execute("update user_item set 西米=西米+1 where user=%s ", [u])
                elif v == '珍珠':
                    cursor.execute("update user_item set 珍珠=珍珠+1 where user=%s ", [u])
                elif v == '布丁':
                    cursor.execute("update user_item set 布丁=布丁+1 where user=%s ", [u])

                conn.commit()
                return render(request, 'calorie.html', locals())
            else:
                pastuser = nowuser
                calsum = 0
                mid_sum = 0
                big_sum = 0
                sum = 0
                if name == '芋圆':
                    calsum += (num / 100) * 135
                elif name == '奥利奥':
                    calsum += (num / 100) * 490
                elif name == '椰果':
                    calsum += (num / 100) * 241
                elif name == '红豆':
                    calsum += (num / 100) * 224
                elif name == '仙草':
                    calsum += (num / 100) * 61
                elif name == '椰子冻':
                    calsum += (num / 100) * 330
                elif name == '奶盖':
                    calsum += (num / 100) * 390
                elif name == '西米':
                    calsum += (num / 100) * 358
                elif name == '珍珠':
                    calsum += (num / 100) * 81
                elif name == '布丁':
                    calsum += (num / 100) * 174
                elif name == '花生麻薯':
                    calsum += (num / 100) * 203
                elif name == '寒天':
                    calsum += (num / 100) * 42
                elif name == '燕麦':
                    calsum += (num / 100) * 367
                elif name == '咖啡冻':
                    calsum += (num / 100) * 56
                elif name == '芋泥':
                    calsum += (num / 100) * 171
                elif name == '芝麻芋圆':
                    calsum += (num / 100) * 37
                elif name == '抹茶芋圆':
                    calsum += (num / 100) * 110
                elif name == '布蕾':
                    calsum += (num / 100) * 251
                elif name == '茶冻':
                    calsum += (num / 100) * 38
                elif name == '熟糯米':
                    calsum += (num / 100) * 348
                elif name == '薏仁':
                    calsum += (num / 100) * 361
                sum += calsum
                big_sum = round((sum + 458.5), 2)
                mid_sum = round((sum + 327.5), 2)
                big_rest = round(big_sum - 270, 2)
                mid_rest = round(mid_sum - 270, 2)

                alltip = "您可通过以下方式消耗过剩的卡路里："
                bsport1 = round(big_rest / 900, 1)
                bsport2 = round(big_rest / 600, 1)
                bsport3 = round(big_rest / 700, 1)
                bsport4 = round(big_rest / 400, 1)
                bsport5 = round(big_rest / 650, 1)
                bsport6 = round(big_rest / 700, 1)
                bsport7 = round(big_rest / 450, 1)
                bsport8 = round(big_rest / 400, 1)

                msport1 = round(mid_rest / 900, 1)
                msport2 = round(mid_rest / 600, 1)
                msport3 = round(mid_rest / 700, 1)
                msport4 = round(mid_rest / 400, 1)
                msport5 = round(mid_rest / 650, 1)
                msport6 = round(mid_rest / 700, 1)
                msport7 = round(mid_rest / 450, 1)
                msport8 = round(mid_rest / 400, 1)

                # 获取calculate.html中的输入值(包括用户值，小料的名称，数量值)
                u = request.POST.get('username')
                v = request.POST.get('ingredients_choice')
                d = request.POST.get('ingredients_quantity')
                # 创建连接
                conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                                       db='milk', charset='utf8')
                # 创建游标
                cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

                # 执行SQL
                cursor.execute("update paint set sum=sum+1 where ingredients_choice=%s", [v])
                conn.commit()

                # 关闭游标
                conn.close()
                # 关闭连接
                cursor.close()

                # 创建连接
                conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',
                                       db='milk', charset='utf8')
                # 创建游标
                cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

                # 算法————————樊蕾靓
                # 执行SQL
                if v == '芋圆':
                    cursor.execute("update user_item set 芋圆=芋圆+1 where user=%s ", [u])
                elif v == '奥利奥':
                    cursor.execute("update user_item set 奥利奥=奥利奥+1 where user=%s ", [u])
                elif v == '椰果':
                    cursor.execute("update user_item set 椰果=椰果+1 where user=%s ", [u])
                elif v == '红豆':
                    cursor.execute("update user_item set 红豆=红豆+1 where user=%s ", [u])
                elif v == '仙草':
                    cursor.execute("update user_item set 仙草=仙草+1 where user=%s ", [u])
                elif v == '椰子冻':
                    cursor.execute("update user_item set 椰子冻=椰子冻+1 where user=%s ", [u])
                elif v == '奶盖':
                    cursor.execute("update user_item set 奶盖=奶盖+1 where user=%s ", [u])
                elif v == '西米':
                    cursor.execute("update user_item set 西米=西米+1 where user=%s ", [u])
                elif v == '珍珠':
                    cursor.execute("update user_item set 珍珠=珍珠+1 where user=%s ", [u])
                elif v == '布丁':
                    cursor.execute("update user_item set 布丁=布丁+1 where user=%s ", [u])

                conn.commit()
                return render(request, 'calorie.html', locals())
        else:
            message="请按要求输入！"
            nowuser = request.POST['username']
            name = request.POST['ingredients_choice']
            num = 0

            calsum=0
            mid_sum = 0
            big_sum = 0
            sum = 0
            if name == '芋圆':
                calsum += (num / 100) * 135
            elif name == '奥利奥':
                calsum += (num / 100) * 490
            elif name == '椰果':
                calsum += (num / 100) * 241
            elif name == '红豆':
                calsum += (num / 100) * 224
            elif name == '仙草':
                calsum += (num / 100) * 61
            elif name == '椰子冻':
                calsum += (num / 100) * 330
            elif name == '奶盖':
                calsum += (num / 100) * 390
            elif name == '西米':
                calsum += (num / 100) * 358
            elif name == '珍珠':
                calsum += (num / 100) * 81
            elif name == '布丁':
                calsum += (num / 100) * 174
            elif name == '花生麻薯':
                calsum += (num / 100) * 203
            elif name == '寒天':
                calsum += (num / 100) * 42
            elif name == '燕麦':
                calsum += (num / 100) * 367
            elif name == '咖啡冻':
                calsum += (num / 100) * 56
            elif name == '芋泥':
                calsum += (num / 100) * 171
            elif name == '芝麻芋圆':
                calsum += (num / 100) * 37
            elif name == '抹茶芋圆':
                calsum += (num / 100) * 110
            elif name == '布蕾':
                calsum += (num / 100) * 251
            elif name == '茶冻':
                calsum += (num / 100) * 38
            elif name == '熟糯米':
                calsum += (num / 100) * 348
            elif name == '薏仁':
                calsum += (num / 100) * 361
            sum += calsum
            big_sum = round(sum + 458.5, 2)
            mid_sum = round(sum + 327.5, 2)
            big_rest = round(big_sum - 270, 2)
            mid_rest = round(mid_sum - 270, 2)

            alltip = "您可通过以下方式消耗过剩的卡路里："
            bsport1 = round(big_rest / 900, 1)
            bsport2 = round(big_rest / 600, 1)
            bsport3 = round(big_rest / 700, 1)
            bsport4 = round(big_rest / 400, 1)
            bsport5 = round(big_rest / 650, 1)
            bsport6 = round(big_rest / 700, 1)
            bsport7 = round(big_rest / 450, 1)
            bsport8 = round(big_rest / 400, 1)

            msport1 = round(mid_rest / 900, 1)
            msport2 = round(mid_rest / 600, 1)
            msport3 = round(mid_rest / 700, 1)
            msport4 = round(mid_rest / 400, 1)
            msport5 = round(mid_rest / 650, 1)
            msport6 = round(mid_rest / 700, 1)
            msport7 = round(mid_rest / 450, 1)
            msport8 = round(mid_rest / 400, 1)
        return render(request, 'calorie.html', locals())
