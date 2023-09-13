from django.urls import path
from .views import *
urlpatterns=[
    path('reg',Regview.as_view(),name='regg'),
    path('home',Custhomeview.as_view(),name='custhome'),
    
    
    

    
]