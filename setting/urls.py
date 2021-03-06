"""lqcharacter2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import rect

# -*- coding: utf-8 -*-
import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index_prod.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^api/', include('api.urls')),
    #url(r'^rect/', include('rect.urls')), # todo 1227 转移到/api/rect/下统一管理. 有非API的使用时再打开.
    url(r'^auth/', include("jwt_auth.urls", namespace="api-auth")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
