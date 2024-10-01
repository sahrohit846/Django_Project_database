from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views
from django.urls import path # type: ignore
# from .views import ResetPasswordView
from django.contrib.auth import views as auth_views # type: ignore
from .views import reset_password
urlpatterns = [
    
    path('', views.landing_page, name ='landing'),
    
    path('home', views.user_dashboard, name='home'),
    
    
    
    path('singup', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('simulator/', views.HomePage, name='simulator'),
    path('logout/', views.LogoutPage, name='logout'),
    # path('forgot_email/', views.ForgotEmailView, name='forgot_email'),
    path('forgot_password/', views.ForgotPasswordView, name='forgot_password'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    
    path('reset-password/', views.reset_password, name='reset_password'),  
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='reset_password.html'
        ), 
        name='reset_password'
    ),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ), 
        name='password_reset_done'
    ),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
        ), 
        name='password_reset_confirm'
    ),
    path('reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'
    ),

    # OTP verification URL (assuming a custom view for OTP verification)
    path('verify_otp/', views.verify_otp, name='verify_otp'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    
    path("simulator",views.simulator,name='simulator'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("quantum_grocery", views.quantum_grocery, name='quantum_grocery')
]   
