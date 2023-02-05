from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('register',views.register,name='register'),
    path('register/main',views.main2,name='main'),
    path('sign_in/main',views.main,name='main'),
    path('sign_in/logout',views.logout,name='logout')

]
