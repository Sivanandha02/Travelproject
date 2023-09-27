from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo2,name='demo2')
]