from django.db.models import F
from django.shortcuts import render
from .models import Circle
from django.http import HttpResponseRedirect
import pymysql
user_name=""
def load(request):
    global user_name
    if request.method == 'GET':
        return render(request, 'load.html')
    elif  request.method=='POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='milk', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        row = cursor.execute("select * from  paint where username=%s and password=%s",
                             (user_name, pass_word))
        res = cursor.fetchone()
        cursor.close()
        conn.close()
        if res:
            allsaying
            return HttpResponseRedirect('/circle/friend')
        else:
            error_msg = '用户名或密码错误'
            return render(request, 'load.html', locals())

def allsaying(request):
    global user_name
    if request.method=='GET':
        num = Circle.objects.all().count()
        if num > 300:
            all = Circle.objects.filter(id=(num - 300, num)).order_by('-id')
        else:
            all = Circle.objects.all().order_by('-id')
        return render(request, 'circle.html', locals())

    elif request.method=='POST':
        if request.POST['saying']:
            getsaying=request.POST['saying']
        else:
            return HttpResponseRedirect('/circle/friend')
        db=Circle()
        db.user=user_name
        db.saying=getsaying
        db.like=0
        db.save()
        return HttpResponseRedirect('/circle/friend')

def add_like(request,likeid):
        num = Circle.objects.all().count()
        if num > 300:
            all = Circle.objects.filter(id=(num - 300, num))
        else:
            all = Circle.objects.all()
        likesaying=Circle.objects.get(id=likeid)
        likesaying.like=F('like')+1
        likesaying.save()
        return HttpResponseRedirect('/circle/friend',locals())