from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'),
    path('upload/', views.upload, name='upload'),
    path('predict/', views.predict, name='predict'),
    path('visualize/', views.visualize, name='visualize'),
    path('logout/', views.logout, name='logout'),
]
