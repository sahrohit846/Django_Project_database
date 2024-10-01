
from django import forms

# for email
class EmailForm(forms.Form):
    email = forms.EmailField(label='Enter your email', max_length=100,      widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))

# for otp 
class OTPForm(forms.Form):
    otp = forms.CharField(label='Enter OTP', max_length=6,        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the 6-digit OTP'}))
    # email = forms.EmailField(label='Enter your email', max_length=100)
    # password = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    
    # def clean(self):


# for password
class SetPasswordForm(forms.Form):
    password = forms.CharField(label='Enter new password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}),
        min_length=8  # Password should have a minimum length for security
    )
    confirm_password = forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}),
        min_length=8
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        # Check if the two passwords match
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match')
        return cleaned_data
        
        
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_decode
# from django.contrib.auth import get_user_model
# from django.views import View
# from .forms import EmailForm, OTPForm, SetPasswordForm

# UserModel = get_user_model()

# class ResetPasswordView(View):
#     def get(self, request, uidb64=None, token=None):
#         # Render the password reset form
#         form = SetPasswordForm()
#         return render(request, 'forgot_password.html', {'form': form})

#     def post(self, request, uidb64=None, token=None):
#         form = SetPasswordForm(request.POST)
#         if form.is_valid():
#             # Process password reset
#             try:
#                 uid = urlsafe_base64_decode(uidb64).decode()
#                 user = UserModel._default_manager.get(pk=uid)
#             except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
#                 user = None

#             if user is not None and default_token_generator.check_token(user, token):
#                 user.set_password(form.cleaned_data['password'])
#                 user.save()
#                 return redirect('password_reset_complete')  # or some success page
#         return render(request, 'forgot_password.html', {'form': form})




































# from django import forms

# # For email
# class EmailForm(forms.Form):
#     email = forms.EmailField(
#         label='Enter your email', 
#         max_length=100,
#         widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
#     )

# # For OTP
# class OTPForm(forms.Form):
#     otp = forms.CharField(
#         label='Enter OTP', 
#         max_length=6,
#         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the 6-digit OTP'})
#     )

# # For setting a new password
# class SetPasswordForm(forms.Form):
#     password = forms.CharField(
#         label='Enter new password', 
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}),
#         min_length=8  # Password should have a minimum length for security
#     )
#     confirm_password = forms.CharField(
#         label='Confirm new password', 
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}),
#         min_length=8
#     )
    
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')

#         # Check if the two passwords match
#         if password != confirm_password:
#             raise forms.ValidationError('Passwords do not match. Please try again.')

#         return cleaned_data
