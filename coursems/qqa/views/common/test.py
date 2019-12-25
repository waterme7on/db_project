from django.http import HttpResponse
from qqa.models import Course
from django.shortcuts import get_object_or_404, render

def index(request):
    return render(request,'base.html',{})