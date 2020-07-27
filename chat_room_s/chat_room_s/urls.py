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
from django.http import JsonResponse
from django.urls import path
from data_base import base


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


urlpatterns = [
    path('login', login)
]
