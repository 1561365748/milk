from django.shortcuts import render
from django.http import HttpResponseRedirect
prosum=0
def pro(request):
    global prosum
    if request.method=='GET':
        prosum=0
        big_sum = round(22, 2)
        mid_sum = round(18, 2)
        big_tip = ""
        mid_tip = ""
        if big_sum >= 3.5:
            big_tip = "大杯中蛋白质含量符合标准，可以食用哦！"
        elif big_sum < 3.5:
            big_tip = "大杯蛋白质含量不符合标准，建议您像商家说明或者根据自己的要求适当调整小料的量"

        if mid_sum > 2.5:
            mid_tip = "中杯中蛋白质含量符合标准，可以食用哦！"
        elif mid_sum <= 2.5:
            mid_tip = "中杯蛋白质含量不符合标准，建议您像商家说明或者根据自己的要求适当调整小料的量"
        return render(request, 'protein.html', locals())

    elif request.method=='POST':
        if request.POST['ingredients_quantity']=='':
            message="请输入小料及数量！"
            prosum = 0
            big_sum = round(22, 2)
            mid_sum = round(18, 2)
            big_tip = ""
            mid_tip = ""
            if big_sum >= 3.5:
                big_tip = "大杯中蛋白质含量符合标准，可以食用哦！"
            elif big_sum < 3.5:
                big_tip = "大杯蛋白质含量不符合标准，建议您像商家说明或者根据自己的要求适当调整小料的量"

            if mid_sum > 2.5:
                mid_tip = "中杯中蛋白质含量符合标准，可以食用哦！"
            elif mid_sum <= 2.5:
                mid_tip = "中杯蛋白质含量不符合标准，建议您像商家说明或者根据自己的要求适当调整小料的量"
            return render(request, 'protein.html', locals())
        elif request.POST['ingredients_quantity'] != '':
            message = ""
            name=request.POST['ingredients_choice']
            num=float(request.POST['ingredients_quantity'])
            mid_sum = 0
            big_sum = 0
            psum=0
            if name=='芋圆':
                prosum+=(num/100)*0.92
            elif name == '奥利奥':
                prosum+=(num/100)*4.8
            elif name == '椰果':
                prosum+=(num/100)*0.85
            elif name == '红豆':
                prosum+=(num/100)*0
            elif name == '仙草':
                prosum += (num / 100) * 0
            elif name == '布丁':
                prosum+=(num/100)*0
            elif name == '西米':
                prosum+=(num/100)*0.04
            elif name == '珍珠':
                prosum+=(num/100)*0
            elif name == '奶盖':
                prosum+=(num/100)*2.06
            elif name == '花生麻薯':
                prosum+=(num/100)*2.53
            elif name == '寒天':
                prosum+=(num/100)*0
            elif name == '燕麦':
                prosum+=(num/100)*0
            elif name == '咖啡冻':
                prosum+=(num/100)*0
            elif name == '芋泥':
                prosum+=(num/100)*1.27
            elif name == '芝麻芋圆':
                prosum += (num / 100) * 0.83
            elif name == '抹茶芋圆':
                prosum+=(num/100)*0.6
            elif name == '布蕾':
                prosum+=(num/100)*5.43
            elif name == '茶冻':
                prosum+=(num/100)*0.16
            elif name == '椰子冻':
                prosum+=(num/100)*2.1
            elif name == '熟糯米':
                prosum+=(num/100)*7.3
            elif name == '薏仁':
                prosum+=(num/100)*12.8
            psum+=prosum
            big_sum = round(psum + 22,2)
            mid_sum = round(psum + 18,2)

            big_tip = ""
            mid_tip = ""
            if big_sum >= 3.5:
                big_tip = "大杯中蛋白质含量符合标准，可以食用哦！"
            elif big_sum <3.5:
                big_tip = "大杯蛋白质含量不符合标准，建议您像商家说明或者根据自己的要求适当调整小料的量"

            if mid_sum > 2.5:
                mid_tip = "中杯中蛋白质含量符合标准，可以食用哦！"
            elif mid_sum <= 2.5:
                mid_tip = "中杯蛋白质含量不符合标准，建议您像商家说明或者根据自己的要求适当调整小料的量"
            return render(request, 'protein.html', locals())
