from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("quotes.urls")),
    path('', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', include('quotes.urls')),
    path('home/', include('quotes.urls')),
    path('create/', include('users.urls')),
]
