from . import views
from django.urls import path

urlpatterns = [

    path('register',views.demo3,name='demo3'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]