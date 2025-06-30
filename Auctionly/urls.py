from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('' , home , name="home"),
    path('sign_in', sign_in, name="sign_in"),
    path('sign_up', sign_up, name="sign_up"),
    path('success', success, name="success"),
    path('verify/<auth_token>', verify , name="verify"),
    path('aboutAuctionly', aboutAuctionly, name="aboutAuctionly"),
    path('contactUs', contactUs, name="contactUs"),
    path('departmentAuctionly', departmentAuctionly, name="departmentAuctionly"),
    path('liveauction', liveauction, name="liveauction"),
    path('pastauction', pastauction, name="pastauction"),
    path('upcomingauction', upcomingauction, name="upcomingauction"),
    path('emailsent', emailsent, name="emailsent"),
    path('modernart', modernart, name="modernart"),
    path('timepieces/', views.timepieces, name='timepieces'),
    path('furniture/', views.furniture, name='furniture'),
    path('aboutAuctionly/', views.aboutAuctionly, name='aboutAuctionly'),
    path('departmentAuctionly/', views.departmentAuctionly, name='departmentAuctionly'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('liveauction/', views.liveauction, name='liveauction'),
    path('upcomingauction/', views.upcomingauction, name='upcomingauction'),
    path('pastauction/', views.pastauction, name='pastauction'),
    path('departmentAuctionly/modernart/', views.modernart, name='modernart'),
    path('departmentAuctionly/timepieces/', views.timepieces, name='timepieces'),
    path('departmentAuctionly/furniture/', views.furniture, name='furniture'),
    path('logout', views.logout_view, name='logout'),
    path('openpage/<int:id>/', openpage, name="openpage"),
    path('test-auction-email/', views.trigger_auction_check, name='test_email'),
    path('departmentAuctionly/jewellery/', views.jewellery, name='jewellery'),
    path('jewellery/', views.jewellery, name='jewellery'),
    path('furniture/', views.furniture, name='furniture'),





    
   


    
]




