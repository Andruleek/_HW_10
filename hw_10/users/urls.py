from django.urls import path
from users import views

urlpatterns = [
    
    path('', views.exit, name='exit'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login')
]