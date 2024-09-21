from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import generate_token  # Removed the redundant import
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
from django.db import IntegrityError


def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if password != confirm_password:
            messages.warning(request, "Passwords do not match.")
            return render(request, 'signup.html', {'email': email})

        try:
            if User.objects.filter(username=email).exists():
                messages.info(request, "Email is already taken.")
                return render(request, 'signup.html', {'email': email})

            user = User.objects.create_user(username=email, email=email, password=password)
            user.is_active = False
            user.save()

            email_subject = "Activate Your Account"
            message = render_to_string('activate.html', {
                'user': user,
                'domain': request.get_host(),
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user),
            })
            email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
            email_message.send()

            messages.success(request, "Activate your account by clicking the link sent to your email.")
            return redirect('signup')  # Redirect to login after signup
        
        except IntegrityError:
            messages.error(request, "There was a problem creating your account. Please try again.")
            return render(request, 'signup.html', {'email': email})

    return render(request, 'signup.html')

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and generate_token.check_token(user, token):
            if not user.is_active:
                user.is_active = True
                user.save()
                messages.success(request, "Your account has been activated successfully.")
            else:
                messages.info(request, "Your account is already activated.")
        else:
            messages.error(request, "The activation link is invalid or has expired.")

        return redirect('login')

def handlelogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the index page on successful login
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html', {'error': "Invalid email or password."})
    
    return render(request, "login.html")

def handlelogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')
