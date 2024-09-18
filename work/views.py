from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import login, signup
from datetime import datetime
import openai
from django.conf import settings

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email already exists
        if signup.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered. Try login')
            return render(request, 'signup.html')

        # If email is unique, save the user information
        signupinfo = signup(
            name=name, 
            email=email, 
            password=password,  # Hash the password
            date=datetime.today()
        )
        signupinfo.save()

        messages.success(request, 'You have successfully signed up! Please log in.')
        return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.method == "get":
        email = request.POST.get('email')
        password = request.POST.get('address')

        logininfo = login(email=email, password=password, date=datetime.today())
        logininfo.save()

        return redirect('home')
    return render(request, 'login.html')

def home(request):
    return render(request, 'homepage.html')

def document(request):
    return render(request, 'document.html')

def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Answer the following question related to Cyber Security: {user_message}",
            max_tokens=150
        )
        chatbot_response = response.choices[0].text.strip()
        return JsonResponse({'response': chatbot_response})
    return render(request, 'chatbot.html')