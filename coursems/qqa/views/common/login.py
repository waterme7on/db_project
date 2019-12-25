from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.hashers import make_password, check_password

def login(request):
    