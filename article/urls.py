from django.contrib import admin
from django.urls import path
from django.conf.urls import handler400, handler500
from . import views
app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('article/<slug:slug>/',views.detail,name = "detail"),
    path('',views.articles,name = "articles"),
]
