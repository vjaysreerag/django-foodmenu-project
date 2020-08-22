from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns=[
  path('',views.home,name='home'),
  path('indian/',views.indian,name='indian'),
  path('chinese/',views.chinese,name='chinese'),
  path('indian/vegindian/',views.vegindian,name='vegindian'),
]  