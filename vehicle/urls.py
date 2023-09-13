"""
URL configuration for vehicle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from account.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/',include('account.urls')),
    path('customer/',include('customer.urls')),
    path('',Logview.as_view(),name="home"),
    path('abo',AboutHomeView.as_view(),name="abo"),
    path('hm',Custhomeview.as_view(),name="hm"),

    
    path('new',ServiceHomeView.as_view(),name='new'),
    path('reg',RegHomeView.as_view(),name='reg'),
    path('char',ChargeHomeView.as_view(),name='char'),
    path('serv',StationHomeView.as_view(),name='serv'),
    path('hel',HelpHomeView.as_view(),name='hel'),

    path('reg',RegHomeView.as_view(),name='reg'),
    path('pay',paymentView.as_view(),name='pay'),
    path('lgout',LgoutView.as_view(),name='lgout')


    



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
