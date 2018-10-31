from django.urls import path
from accounts import views


app_name = 'auth'

urlpatterns = [
    path('', views.login_view, name='accounts_login'),
    path('logout/', views.logout_view, name='accounts_logout'),
    path('register/', views.register, name='accounts_register'),
]
