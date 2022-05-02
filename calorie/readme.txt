
/calorie:.   //实现计算卡路里的功能
│  admin.py //可以自定义django管理工具，此处为空
│  apps.py  //包含对应用calorie的配置
│  models.py //应用calorie的数据类型,此处为空
│  readme.txt 
│  tests.py  //该文件中可以编写测试文档来测试所建立的应用，此处为空。
│  urls.py  //用来声明并调用在views.py中的新建的方法（cal、similarity、recommandList）
│  views.py //保存响应各种请求的函数，实现计算卡路里的功能，使用HTTPResponse返回页面所需数据。
│  __init__.py
│  
├─migrations //创建calorie应用时自动创建
│  │  __init__.py
│  │  
│  └─__pycache__ 
│          __init__.cpython-38.pyc
│          
└─__pycache__  //编译后自动创建
        admin.cpython-38.pyc
        apps.cpython-38.pyc
        models.cpython-38.pyc
        urls.cpython-38.pyc
        views.cpython-38.pyc
        __init__.cpython-38.pyc
        
