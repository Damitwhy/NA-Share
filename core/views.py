from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
# from .models import Post
from .models import Share
from .forms import CommentForm

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

# custom view for comments
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