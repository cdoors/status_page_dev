from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import subprocess
import sys
from pydantic import BaseModel, ValidationError, Field


# Create your views here.

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'status_page/login.html', {'error': 'Invalid credentials'})
#     return render(request, 'status_page/login.html')

# @login_required
def home(request):
    return render(request, 'status_page/home.html')

# @login_required
def submit(request):
    if request.method == 'POST':
        hhnbr = request.POST.get('hhnbr')
        email = request.POST.get('email')

        # Validation
        class RawData(BaseModel):
            hhnbr: int = Field(..., ge=100000, lt=1000000)
            email: str = Field(..., pattern=r'.*@.*')

        class DataPackage(BaseModel):
            raw_data: RawData

        try:
            data = DataPackage(raw_data=RawData(hhnbr=hhnbr, email=email))
        except ValidationError as e:
            error_messages = []
            for error in e.errors():
                field = error['loc'][-1]
                message = error['msg']
                error_messages.append(f"{field.capitalize()}: {message}")
            return render(request, 'status_page/error.html', {'errors': error_messages})
        
        # Run the side_script.py
        subprocess.run([sys.executable, 'side_script.py', hhnbr, email], check=True)
        
        return render(request, 'status_page/submit.html')
    return redirect('home')

# Add this function to the existing views.py file
def error(request):
    errors = request.GET.getlist('errors')
    return render(request, 'status_page/error.html', {'errors': errors})
