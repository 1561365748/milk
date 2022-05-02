/milk:.  //主文件
│  asgi.py
│  readme.txt
│  settings.py  //包括了项目的初始化设置，可以针对整个项目进行有关参数配置，比如配置数据库、添加应用等。
│  urls.py  //用来声明并调用在views.py中的新建的方法。
│  view.py   //用户保存响应各种请求的函数或者类。创建一个可供页面调用并返回数据的方法，使用HTTPResponse返回页面所需数据。
│  wsgi.py  //wsgi.py定义所创建的项目都是WSGI应用。
│  __init__.py
│  
└─__pycache__  //编译后自动创建
        settings.cpython-38.pyc
        urls.cpython-38.pyc
        view.cpython-38.pyc
        wsgi.cpython-38.pyc
        __init__.cpython-38.pyc
        

