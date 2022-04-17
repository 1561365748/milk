from turtle import pd
import pymysql
from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
def main(request):
    if request.method == 'GET':
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='milk', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select ingredients_choice from paint")
        ingredients_list = [item['ingredients_choice'] for item in cursor.fetchall()]
        cursor.execute("select sum from paint")
        ingredients_like =[item['sum'] for item in cursor.fetchall()]
        cursor.close()
        conn.close()
        #显示中文
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        # 修改图的大小
        plt.figure(dpi=111)
        #y轴转化为np类型数组
        y=np.asarray(ingredients_like)
        plt.bar(ingredients_list,y,color='Deepskyblue')
        plt.title('小料受欢迎程度')
        #保存
        #plt.savefig( "D:\python\Django-2.2.24\milk\static\img\like.png")
        plt.savefig('D:\python\Django-2.2.24\milk\static\img\like.png')
        return render(request,'main.html')

