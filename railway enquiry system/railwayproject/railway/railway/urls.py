"""railway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from unicodedata import name
from django.contrib import admin
from django.urls import re_path,include
from myapp import views
urlpatterns = [
    re_path('admin/', admin.site.urls),
    #re_path(r'^index$',views.index,name='index'),
    re_path(r'^admin_signup/$',views.admin_signup,name='admin_signup'),
    re_path(r'^user_signup/$',views.user_signup,name='user_signup'),
    re_path(r'^t_registration$',views.t_registration,name='t_registration'),
    re_path(r'^t_display$',views.t_display,name='t_display'),
    re_path(r'^bticket$',views.bticket,name='bticket'),
    re_path(r'^u_t_display$',views.u_t_display,name='u_t_display'),
    re_path(r'^book(?P<pk>\d+)$',views.book,name='book'),
    re_path(r'^cancel(?P<pk>\d+)$',views.cancel,name='cancel'),
    re_path(r'^search$',views.search,name='search'),
    re_path(r'^delete(?P<pk>\d+)/$',views.delete,name='delete'),
    re_path(r'^billing$',views.billings,name='billing'),
    re_path(r'^submit$',views.submit,name='submit'),
    re_path(r'^adminuser_login$',views.adminuser_login,name='adminuser_login'),
    re_path(r'^adminuser_logout$',views.adminuser_logout,name='adminuser_logout'),
    re_path(r'^bookticket2$',views.bookticket2,name='bookticket2'),
    re_path(r'^userviewticket$',views.userviewticket,name='userviewticket'),  
    re_path(r'^user_signup$',views.user_signup,name='user_signup'),
    re_path(r'^viewticket$',views.viewticket,name='viewticket'),
    re_path(r'^payement$',views.payement,name='payement'),
    re_path(r'^admindata$',views.admindata,name='admindata'),
    re_path(r'^search1$',views.search1,name='search1'),
    re_path(r'^$',views.bookticket,name='bookticket'),
    
    
]
