from django.shortcuts import render
from django.http import HttpResponseRedirect
carsum=0
def car(request):
    global carsum
    if request.method=='GET':
        carsum=0
        big_sum = round(46, 2)
        mid_sum = round(33, 2)
        big_tip = ""
        mid_tip = ""
        if big_sum > 50:
            big_tip = "大杯已经超过了人体一天糖类的最大摄入量，建议您减少所加小料的量或者删除部分加入的小料。"
        elif big_sum <= 25:
            big_tip = "大杯糖类含量符合标准，可以食用，但要注意今日其他食物的摄入哦！"
        elif big_sum > 25 and big_sum <= 50:
            big_tip = "大杯所含糖类未超过人体一天糖类的最大摄入量，但大于一天的建议摄入量，您可根据自己的要求适当调整小料的量"

        if mid_sum > 50:
            mid_tip = "中杯已经超过了人体一天糖类的最大摄入量，建议您减少所加小料的量或者删除部分加入的小料。"
        elif mid_sum <= 25:
            mid_tip = "中杯糖类含量符合标准，可以食用，但要注意今日其他食物的摄入哦！"
        elif mid_sum > 25 and mid_sum <= 50:
            mid_tip = "中杯所含糖类未超过人体一天糖类的最大摄入量，但大于一天的建议摄入量，您可根据自己的要求适当调整小料的量"
        return render(request, 'carbon.html', locals())

    elif request.method=='POST':
        if request.POST['ingredients_quantity']=='':
            message = "请输入小料及数量！"
            carsum = 0
            big_sum = round(46, 2)
            mid_sum = round(33, 2)
            big_tip = ""
            mid_tip = ""
            if big_sum > 50:
                big_tip = "大杯已经超过了人体一天糖类的最大摄入量，建议您减少所加小料的量或者删除部分加入的小料。"
            elif big_sum <= 25:
                big_tip = "大杯糖类含量符合标准，可以食用，但要注意今日其他食物的摄入哦！"
            elif big_sum > 25 and big_sum <= 50:
                big_tip = "大杯所含糖类未超过人体一天糖类的最大摄入量，但大于一天的建议摄入量，您可根据自己的要求适当调整小料的量"

            if mid_sum > 50:
                mid_tip = "中杯已经超过了人体一天糖类的最大摄入量，建议您减少所加小料的量或者删除部分加入的小料。"
            elif mid_sum <= 25:
                mid_tip = "中杯糖类含量符合标准，可以食用，但要注意今日其他食物的摄入哦！"
            elif mid_sum > 25 and mid_sum <= 50:
                mid_tip = "中杯所含糖类未超过人体一天糖类的最大摄入量，但大于一天的建议摄入量，您可根据自己的要求适当调整小料的量"
            return render(request, 'carbon.html', locals())
        elif request.POST['ingredients_quantity']!='':
            message=""
            name=request.POST['ingredients_choice']
            num=float(request.POST['ingredients_quantity'])

            mid_sum = 0
            big_sum = 0
            csum=0
            if name=='芋圆':
                csum += (num / 100) * 52.14
            elif name == '奥利奥':
                csum += (num / 100) * 67.8
            elif name == '椰果':
                csum += (num / 100) * 5.93
            elif name == '红豆':
                csum += (num / 100) * 17.25
            elif name == '仙草':
                csum += (num / 100) * 13.7
            elif name == '布丁':
                csum += (num / 100) * 17
            elif name == '西米':
                csum += (num / 100) * 17.74
            elif name == '珍珠':
                csum += (num / 100) * 20.25
            elif name == '奶盖':
                csum += (num / 100) * 9.6
            elif name == '花生麻薯':
                csum += (num / 100) * 43.17
            elif name == '寒天':
                csum += (num / 100) * 1.16
            elif name == '燕麦':
                csum += (num / 100) * 20
            elif name == '咖啡冻':
                csum += (num / 100) * 14
            elif name == '芋泥':
                csum += (num / 100) * 20.24
            elif name == '芝麻芋圆':
                csum += (num / 100) * 25.55
            elif name == '抹茶芋圆':
                csum += (num / 100) * 26.52
            elif name == '布蕾':
                csum += (num / 100) * 9.48
            elif name == '茶冻':
                csum += (num / 100) * 9.15
            elif name == '椰子冻':
                csum += (num / 100) * 5.66
            elif name == '熟糯米':
                csum += (num / 100) * 78.3
            elif name == '薏仁':
                csum += (num / 100) * 66.5
            csum+=carsum
            big_sum = round(csum + 46, 2)
            mid_sum =round(csum + 33 ,2)

            big_tip=""
            mid_tip = ""
            if big_sum>50:
                big_tip="大杯已经超过了人体一天糖类的最大摄入量，建议您减少所加小料的量或者删除部分加入的小料。"
            elif  big_sum<=25:
                big_tip = "大杯糖类含量符合标准，可以食用，但要注意今日其他食物的摄入哦！"
            elif big_sum>25 and big_sum<=50:
                big_tip = "大杯所含糖类未超过人体一天糖类的最大摄入量，但大于一天的建议摄入量，您可根据自己的要求适当调整小料的量"

            if mid_sum>50:
                mid_tip = "中杯已经超过了人体一天糖类的最大摄入量，建议您减少所加小料的量或者删除部分加入的小料。"
            elif mid_sum<=25:
                mid_tip = "中杯糖类含量符合标准，可以食用，但要注意今日其他食物的摄入哦！"
            elif mid_sum >25 and mid_sum<=50:
                mid_tip = "中杯所含糖类未超过人体一天糖类的最大摄入量，但大于一天的建议摄入量，您可根据自己的要求适当调整小料的量"
            return render(request, 'carbon.html', locals())
