from django.http import HttpResponse
from django.template import loader
from .models import Member,BlogModel
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .admin import MemberAdmin
from django.db.models import Q
import PIL
from django.shortcuts import get_list_or_404,render
from django.core import *
from django.views import generic


def light_theme(request):
    return render(request,'light_theme.html')

def dark_theme(request):
     return render(request,'dark_theme.html')

def search(request):
    query=request.GET.get('q','')
    if query:
        results=BlogModel.objects.filter(Q(content__icontains=query)|Q(title__icontains=query)|Q(image__icontains=query))
    else:
        results=[]
    return render(request,'search_results.html',{'results':results,'query':query})

def set_cookie_view(request):
    response = HttpResponse("Cookie has been set!")
    response.set_cookie('my_cookie', 'cookie_value', max_age=3600)  # Cookie expires in 1 hour
    return response

def read_cookie_view(request):
    # Accessing the cookie named 'my_cookie'
    cookie_value = request.COOKIES.get('my_cookie', 'default_value')
    return HttpResponse(f"The value of 'my_cookie' is {cookie_value}")

def delete_cookie_view(request):
    response = HttpResponse("Cookie has been deleted!")
    # Deleting the cookie named 'my_cookie'
    response.delete_cookie('my_cookie')
    return response

def cookie_template_view(request):
    # Fetching the cookie value
    cookie_value = request.COOKIES.get('my_cookie', 'default_value')
    # Passing the cookie value to the template
    return render(request, 'cookie_template.html', {'cookie_value': cookie_value})

def set_cookie_with_options(request):
    response = HttpResponse("Cookie with options has been set!")
    response.set_cookie(
        'my_cookie',                # Cookie name
        'cookie_value',             # Cookie value
        max_age=3600,               # Time in seconds until the cookie expires (1 hour)
        path='/',                   # Path where the cookie is accessible
        domain='example.com',       # Domain for which the cookie is valid
        secure=True,                # Cookie is only sent over HTTPS
        httponly=True,              # Cookie is not accessible via JavaScript
        samesite='Lax'              # SameSite attribute to restrict cross-site requests
    )
    return response