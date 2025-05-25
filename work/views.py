from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import signup, Bugs
from datetime import datetime
import openai
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.contrib.auth.hashers import make_password
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import FileResponse
import cv2
import numpy as np
import os
import random
import base64
from .models import EncryptedFile
from .utils import generate_key
from .forms import EncryptedFileForm
from PIL import Image
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

        messages.success(
            request, 'You have successfully signed up! Please log in.')
        return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Email is already registered. Try login')
            return redirect('login')
    return render(request, 'login.html')


def home(request):
    return render(request, 'homepage.html')


def document(request):
    return render(request, 'document.html')


def broken(request):
    return render(request, 'broken.html')


def authentication(request):
    return render(request, 'authentication.html')


def injection(request):
    return render(request, 'injection.html')


def vulner(request):
    return render(request, 'vulner.html')


def insecure(request):
    return render(request, 'insecure.html')


def security(request):
    return render(request, 'security.html')


def bug(request):
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        website_url = request.POST.get('website_url')
        pricing = request.POST.get('pricing')
        comments = request.POST.get('comments')

        bugs_info = Bugs(
            company_name=company_name,
            email=email,
            website_url=website_url,  # Hash the password
            pricing=pricing,
            comments=comments,
        )
        bugs_info.save()
    return render(request, 'bug.html')


def pentest(request):
    return render(request, 'pentest.html')


def system(request):
    return render(request, 'system.html')


def awareness(request):
    return render(request, 'awareness.html')


def article(request):
    return render(request, 'article.html')

# views.py


def encryption_tool(request):
    if request.method == 'POST':
        form = EncryptedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            original_name = uploaded_file.name

            # Generate a 22-character encryption key
            encrypted_key = generate_key()[:22]

            # Create new filename using the key
            new_filename = f"{encrypted_key}.png"
            save_path = os.path.join(
                settings.BASE_DIR, "static/assets/images", new_filename)

            # Save the file to static folder
            with open(save_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Save file info to admin panel
            EncryptedFile.objects.create(
                file=f"static/assets/images/{new_filename}",
                filename=original_name,
                encrypted_key=encrypted_key
            )

            return render(request, "encryption_tool.html", {
                "file_id": encrypted_key,
                "encrypted_key": encrypted_key
            })
    else:
        form = EncryptedFileForm()

    return render(request, "encryption_tool.html", {"form": form})


def decrypt_tool(request):
    decrypted_file_url = None
    error_message = None

    if request.method == "POST":
        entered_key = request.POST.get("password", "").strip()

        if entered_key:
            filename = f"{entered_key}.png"
            file_path = os.path.join(
                settings.BASE_DIR, "static/assets/images", filename)

            if os.path.exists(file_path):
                # Serve the file for download
                return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
            else:
                error_message = "No file found for this key!"
        else:
            error_message = "Encryption key is required!"

    return render(request, "encryption_tool.html", {
        "error_message": error_message
    })


def podcast(request):
    return render(request, 'podcast.html')


def contact(request):
    return render(request, 'contact.html')


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
