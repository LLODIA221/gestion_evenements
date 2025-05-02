from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from evenements.views import dashboard, register

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('evenements/', include('evenements.urls')),
    
    # Auth
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),
]

