"""py_code URL Configuration

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
from django.contrib import admin
#RESTFul API
from django.conf.urls import url, include
from rest_framework import routers

from tools import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    #RESTFUL API - System
    url(r'^product/', include(router.urls)),
    url(r'^product/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #ADMIN
    url(r'^product/admin/', admin.site.urls),
    url(r'^product/users/$', views.UserList.as_view()),
    url(r'^product/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    #QR_CODE --index
    url(r'^product/qrcode/(.+)$', views.generate_qrcode, name='qrcode'),
    url(r'^product/index.html', views.index, name='index'),
    url(r'^product/search$', views.QueryProductinPc),
    #RESTFUL API- USER PART
    url(r'^api-taozi/wechat/products-all',views.ProuctsList.as_view()),
    url(r'^api-taozi/wechat/product_name=(.+)$',views.QueryProductinMobile),
    url(r'^api-taozi/wechat/product_page=(.+)$', views.GetproductLimit),
    url(r'^api-taozi/wechat/product_check_code=(.+)$', views.CheckTheProductInfo),
    url(r'^api-taozi/wechat/product_id=(.+)$', views.QueryProductinfo),
]
