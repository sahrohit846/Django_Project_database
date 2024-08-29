


from django.core.mail import send_mail
import uuid


def send_forget_password_mail (email):
  token =str(uuid.uuid4())
  subject ='Your forget password link'
  message =f'Hi  CLICK ON THIS LINK TO RESET YOUR PASSWORD http://127.0.0.1:8085/forgot_password/{token}/'