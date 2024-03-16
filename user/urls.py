from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('feedback',views.feedback,name="feedback"),
    path('contact', views.contact_view, name="contact"),
    path('zodiacsign', views.zodiacsign, name="zodiacsign"),
    path('register',views.registration,name="register"),
    path('horoscope', views.horoscope, name="horoscope"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    path('checklogin',views.checklogin,name='userlogin')

]