
from django.shortcuts import render,HttpResponse,redirect
from django.http import FileResponse
import os
from home.models import Contact , User
# from home.models import Profile
from datetime import datetime
from django.utils import timezone
from django.conf import settings



from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
import random
import string
from .models import *

from .helpers import send_forget_password_mail


# Create your views here.
def index(request):
    # messages.sucess(request)
    numbers=list(range(20))
    # return render(request,'simulator.html',context)
    return render(request,'simulator.html',{'numbers':numbers})
def simulator(request):
    numbers=list(range(20))
    # return render(request,'simulator.html',context)
    return render(request,'simulator.html',{'numbers':numbers})
def about(request):
 
    return render(request,'about.html')


from .models import Contact
from datetime import datetime

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
       
        # Create an instance of the Contact model and save it to the database
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        
        messages.success(request, "Your details have been successfully sent!")

        return render(request, 'contact.html')

    else:
        return render(request, 'contact.html')  # Render contact.html for GET requests

def quantum_grocery(request):
 
        return render("Data uploaded Soon ! :)") # type: ignore
    
    
    
#*************************Regitration and login views **********************
def landing_page(request):
    return render(request, 'landing.html')
 
def user_dashboard(request):
    # Check if the user is a superuser (admin)
    # if request.user.is_superuser:
    #     return render(request, 'admin_dashboard.html')  # Separate template for admins
    # else:
    #     return render(request, 'user_dashboard.html')  # For regular users

    return render (request,'home.html')


from django.contrib.auth import logout

def LogoutPage(request):
    logout(request)
    # messages.success(request, "You have been logged out successfully.")
    return redirect('landing')



# from django.contrib.auth.models import Profile


# Create your views here.
@login_required(login_url='login') 
def HomePage(request):
    if request.user.is_superuser:
       return render(request, 'admin.site.urls')  # Separate template for admins
    else:
       return render(request, 'simulator.html')  # For regular users
    # return render(request, 'admin_dashboard.html')
    # return render (request,'simulator.html')



# 
def SignupPage(request):
     # If the user is already logged in, redirect to the home page
    if request.user.is_authenticated:
     return redirect('simulator')
 
    # Check if the request method is POST (i.e., the user submitted the form)
    if request.method == 'POST':
        try:
            # Retrieve the form data from the request
            uname = request.POST.get('username')  # Get the username from the form <name value>
            email = request.POST.get('email')  # Get the email from the form <name value>
            pass1 = request.POST.get('password1')  # Get the password from the form <name value>
            pass2 = request.POST.get('password2')  # Get the confirm password from the form <name value>
            
            # Check if a user with the provided username already exists
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            
            # Check if the email address is valid
            if not email.endswith(settings.EMAIL_DOMAIN):
                messages.error(request, 'Invalid email address')
                return redirect('signup')
            
            # Check if the password meets the required complexity (at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character)
            
            if (len(pass1) < 6 or not any(char.isupper() for char in pass1) or 
                not any(char.islower() for char in pass1) or 
                not any(char.isdigit() for char in pass1) or 
                    not any(char in string.punctuation for char in pass1)):
                    messages.error(request, 'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character')
                    return redirect('signup')
                                                
          
        
            # Check if the passwords match
            if pass1 != pass2:
                # If they don't match, return an error message
                messages.error(request, "Your password and confirm password are not the same!!")
            else:
                # If they match, create a new user
                my_user = User.objects.create_user(uname, email, pass1) # type: ignore
                # Save the new user to the database
                my_user.save()
                messages.success(request, "Your account has been created successfully!")
               
            #    #  store the ojects in profile model
            #     profile_obj= Profile.objects.create(User= my_user)
            #     messages.success(request, "Your account has been created successfully!")
            #     profile_obj.save()
                
                
               
                # Redirect the user to the login page
                return redirect('login')

        except Exception as e:
            # Handle any unexpected errors
            print(e)
            messages.error(request, f"An error occurred during signup: {str(e)}")

    return render(request, 'signup.html')

# login page setup 
# def LoginPage(request):
#     # If the user is already logged in, redirect to the home page
#     if request.user.is_authenticated:
#         return redirect('simulator')
# # If the user is not logged in, display the login page
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('pass')
        
#          # Check if both username and password are not  provided
#         if not username or not pass1:
#             messages.error(request,'Both username & Password are required')
#             return redirect('login')
        
        
#         user=authenticate(request,username=username,password=pass1)
        
#         if user is not None:
           
#             login(request,user)
#             messages.success(request, f' welcome {username} !!')
            
#             return redirect('simulator')
           
#         else:
#             messages.error (request,message="Username or Password is incorrect!!!")
#             return redirect('login')  # Redirect to the login page to show the message

#     return render (request,'login.html')
 
 
 
 
 
#  **********************here authenticate if superuser found then redirect to admin panel other wise user panel(simulator)*******************

# login page setup
def LoginPage(request):
    # If the user is already logged in, redirect based on their role (superuser or regular user)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin:index')  # Redirect superusers to Django admin panel
        else:
            return redirect('home')  # Redirect regular users to the simulator page
        
           # return redirect('simulator')  # Redirect regular users to the simulator page

    # If the user is not logged in, display the login page
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')

        # Check if both username and password are provided
        if not username or not pass1:
            messages.error(request, 'Both username & Password are required')
            return redirect('login')

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
           # messages.success(request, f'Welcome {username} !!')

            # Redirect based on whether the user is a superuser or a regular user
            if user.is_superuser:
                return redirect('admin:index')  # Redirect superusers to the Django admin panel
            else:
                return redirect('home')  # Redirect regular users to the simulator page

        else:
            messages.error(request, "Username or Password is incorrect!!!")
            return redirect('login')  # Redirect to the login page to show the message

    return render(request, 'login.html')

 
  
 
 # View for Forgot Email ID

def ForgotEmailView(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Generate a new password
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.set_password(new_password) # type: ignore
            user.save()
            # Send the new password to the user's email address
            send_mail(
                'Your New Password',
                f'Hello {user.username}, your new password is {new_password}.', # type: ignore
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'A new password has been sent to your email.')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'No user found with that email address.')
            return redirect('forgot_password')
   return render(request, 'forgot_password.html')
 


import random
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import EmailForm
from.forms import OTPForm
def generate_otp():
    return random.randint(100000, 999999)

def send_otp_email(email, otp):
    subject = 'Your OTP for Password Reset'
    message = f'Your OTP for resetting the password is {otp}.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


# View for Forgot Password 
def ForgotPasswordView(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = generate_otp()
            request.session['otp'] = otp
            request.session['email'] = email
            send_otp_email(email, otp)
            messages.success(request, 'OTP sent to your email address.')
            return redirect('verify_otp')
    else:
        form = EmailForm()

    # Ensure the form is passed to the template in both GET and POST cases
    return render(request, 'forgot_password.html', {'form': form})


 
# for getting verify otp view
def verify_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            sent_otp = request.session.get('otp')
            if str(entered_otp) == str(sent_otp):
                # OTP is correct, redirect to password reset page
                return redirect('reset_password')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
    else:
        form = OTPForm()
    return render(request, 'verify_otp.html', {'form': form})





from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import SetPasswordForm

User = get_user_model()

def reset_password(request, uidb64=None, token=None):
    if uidb64 and token:  # This means the user has clicked the link to reset the password
        try:
            uid = force_str(urlsafe_base64_decode(uidb64)) #
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and default_token_generator.check_token(user, token):
            if request.method == 'POST':
                form = SetPasswordForm(request.POST)
                if form.is_valid():
                    password = form.cleaned_data.get('password')
                    user.set_password(password) # type: ignore
                    user.save()
                    update_session_auth_hash(request, user)  # type: ignore # Optional: keeps user logged in after password change
                    messages.success(request, 'Your password has been reset successfully!')
                    return redirect('login')
                else:
                    messages.error(request, 'Please correct the error below.')
            else:
                form = SetPasswordForm()
            return render(request, 'reset_password.html', {'form': form})
        else:
            messages.error(request, 'The reset link is invalid, possibly because it has expired.')
            return redirect('password_reset')

    # If no uidb64 and token are provided, redirect to password reset page
    return redirect('password_reset')
