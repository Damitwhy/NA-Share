from django.shortcuts import render, get_object_or_404
from django.views import generic
# from .models import Post

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'about.html')