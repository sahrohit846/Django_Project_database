from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('simulator/', views.HomePage, name='simulator'),
    path('logout/', views.LogoutPage, name='logout'),
    path('forgot_email/', views.ForgotEmailView, name='forgot_email'),
    path('forgot_password/', views.ForgotPasswordView, name='forgot_password'),
  
    # path("",views.index,name='home'),
    path("simulator",views.simulator,name='simulator'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("quantum_grocery", views.quantum_grocery, name='quantum_grocery')
]   