from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
# from .models import Post
from .models import Share, Comment
from .forms import CommentForm, ShareForm

# Create your views here.
def home(request):
    shares = Share.objects.all()
    return render(request, 'core/home.html', {'shares': shares})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    return render(request, 'core/services.html')

# Comment view
def comment(request, share_id):
    share = get_object_or_404(Share, pk=share_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.share = share
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'core/comment.html', {'form': form, 'share': share})

# Share create view
def create_share(request):
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            share = form.save(commit=False)
            share.user = request.user
            share.save()
            return redirect('home')
    else:
        form = ShareForm()
    return render(request, 'core/create_share.html', {'form': form})