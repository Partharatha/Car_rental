from django.urls import path
from registrationapp import views

urlpatterns = [
    path('', views.registration,name="register"),
    path('login', views.user_login,name="login"),
    path('home', views.home,name="home"),
    path('profile', views.profile,name="profile"),
    path('update',views.update,name='update'),
    path('logout',views.user_logout,name='logout'),
    path('password_reset',views.password_reset,name='password_reset'),
  
]