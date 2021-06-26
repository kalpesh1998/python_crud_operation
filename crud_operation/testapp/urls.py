from django.contrib import admin
from django.urls import path, include
from .views import create_view,list_view,detail_view,update_view,delete_view

urlpatterns = [
    path('info/', create_view),
    path("list/",list_view),
    path("<pid>",detail_view),
    path("<id>/update",update_view),
    path("<id>/delete",delete_view)

]