"""chatr_oom_s URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import json

from django.contrib import admin
from dwebsocket.decorators import accept_websocket
from django.http import JsonResponse
from django.urls import path
from data_base import base

users = []
wss = []


@accept_websocket
def test(request):
    print(request.websocket)
    if request.is_websocket():
        print(request)
        try:
            while 1:
                message = request.websocket.wait()  # 接受前段发送来的数据
                rep_data = ''
                if message:
                    message = eval(bytes.decode(message))
                    print(message)
                    print(type(message))
                    if (message['act'] == 'init'):
                        users.append({
                            'user_name': message['user_name'],
                            'ws': request.websocket
                        })
                        rep_data = {
                            'act': 'message',
                            'message': '连接成功'
                        }
                    print(users)
                    request.websocket.send(json.dumps(rep_data).encode())  # 发送给前段的数据

        except Exception as e:
            for user in users:
                if (user['ws'] == request.websocket):
                    users.remove(user)
            request.websocket.close()
            return


def login(req):
    req_data = json.loads(req.POST.get('data'))
    print(req_data)
    user_name = req_data['user_name']
    user_pwd = req_data['user_pwd']
    print(user_name)
    print(user_pwd)
    sql = "SELECT * FROM user WHERE user_name  = '%s'" % user_name
    results = base.execute_sql(sql, 'select')
    print(results)
    if not results:
        flag = 1
    else:
        print(type(results[0][1]))
        if str(results[0][1]) == user_pwd:
            flag = 0
        else:
            flag = 1

    print(flag)
    data = {
        'flag': flag
    }
    return JsonResponse(data)


def description_offer(req):
    print(req.POST.get('data'))
    req_data = json.loads(req.POST.get('data'))
    print(req_data)
    user_from = req_data['user_from']
    user_to = req_data['user_to']
    description = req_data['description']

    message = {
        'act': 'description_offer',
        'description': description,
        'user_from': user_to,
        'user_to': user_from
    }
    for user in users:
        if (user['user_name'] == user_to):
            user['ws'].send(json.dumps(message).encode())
            break
    return JsonResponse({})


def description_answer(req):
    req_data = json.loads(req.POST.get('data'))

    user_from = req_data['user_from']
    user_to = req_data['user_to']
    description = req_data['description']

    message = {
        'act': 'description_answer',
        'description': description,
        'user_from': user_to,
        'user_to': user_from
    }
    for user in users:
        if user['user_name'] == user_to:
            user['ws'].send(json.dumps(message).encode())
            break
    return JsonResponse({})


def ic_offer(req):
    req_data = json.loads(req.POST.get('data'))
    print(req_data)
    user_from = req_data['user_from']
    user_to = req_data['user_to']
    ic = req_data['ic']

    message = {
        'act': 'ic_offer',
        'ic': ic,
        'user_from': user_to,
        'user_to': user_from
    }
    for user in users:
        if user['user_name'] == user_to:
            user['ws'].send(json.dumps(message).encode())
            break
    return JsonResponse({})


def ic_answer(req):
    req_data = json.loads(req.POST.get('data'))
    print(req_data)
    user_from = req_data['user_from']
    user_to = req_data['user_to']
    ic = req_data['ic']

    message = {
        'act': 'ic_answer',
        'ic': ic,
        'user_from': user_to,
        'user_to': user_from
    }
    for user in users:
        if user['user_name'] == user_to:
            user['ws'].send(json.dumps(message).encode())
            break
    return JsonResponse({})


urlpatterns = [
    path('login', login),
    path('test', test),
    path('description_offer', description_offer),
    path('description_answer', description_answer),
    path('ic_offer', ic_offer),
    path('ic_answer', ic_answer),
]
