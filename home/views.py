
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
 
        return render("Data uploaded Soon ! :)")
    
    



def LogoutPage(request):
    logout(request)
    return redirect('login')

#Regitration and login views 



from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.models import User
# from django.contrib.auth.models import Profile


# Create your views here.
@login_required(login_url='login') 
def HomePage(request):
    return render (request,'simulator.html')



# 
def SignupPage(request):
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
                my_user = User.objects.create_user(uname, email, pass1)
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

    
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        
         # Check if both username and password are not  provided
        if not username or not pass1:
            messages.error(request,'Both username & Password are required')
            return redirect('login')
        
        
        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
           
            login(request,user)
            messages.success(request, f' welcome {username} !!')
            
            return redirect('simulator')
           
        else:
            messages.error (request,message="Username or Password is incorrect!!!")
            return redirect('login')  # Redirect to the login page to show the message

    return render (request,'login.html')
 
 
  
 
 # View for Forgot Email ID

def ForgotEmailView(request):
   if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Generate a new password
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.set_password(new_password)
            user.save()
            # Send the new password to the user's email address
            send_mail(
                'Your New Password',
                f'Hello {user.username}, your new password is {new_password}.',
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
 



# View for Forgot Password 
def ForgotPasswordView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            # Send the registered email ID to the user's email address
            send_mail(
                'Your Registered Email ID',
                f'Hello {user.username}, your registered email ID is {user.email}.',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            messages.success(request, 'Your registered email ID has been sent to your email.')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'No user found with that username.')
            return redirect('forgot_email')
    return render(request, 'forgot_email.html')


#  change password views


def ChangePassword(request , token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change_password/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change_password/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login/')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'change_password.html' , context)
   
 

import uuid
def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget_password/')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('/forget-password/')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'forget_password.html')