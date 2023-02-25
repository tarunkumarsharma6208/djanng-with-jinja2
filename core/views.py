from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    obj = Book.objects.all()
    return render(request, 'index.html.j2', {'obj': obj})