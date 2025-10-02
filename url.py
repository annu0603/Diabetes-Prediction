from django.contrib import admin
from django.urls import path
from . import views 

urlpattern = [
    path('admin/' , admin.site.urls),
    path("",views.home)
]