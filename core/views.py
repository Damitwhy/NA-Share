from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
# from .models import Post
from .models import Share, Comment, Message, User
from .forms import CommentForm, ShareForm, ContactForm
from django.contrib import messages


# Create your views here.


def home(request):
    shares = Share.objects.all()
    return render(request, 'core/home.html', {'shares': shares})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Assuming you have a predefined user for the team
            team_user = User.objects.get(username='Admin')
            message = Message(
                sender=request.user if request.user.is_authenticated else None,
                receiver=team_user,
                content=form.cleaned_data['message']
            )
            message.save()
            messages.success(request, 'Message has been received and we will be in contact soon.')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def services(request):
    return render(request, 'core/services.html')

def stories_detail(request, share_id):
    share = get_object_or_404(Share, id=share_id)
    comments = Comment.objects.filter(share=share)
    return render(request, 'core/stories_detail.html', {'share': share, 'comments': comments})

# Comment view

def comment(request, share_id):
    share = get_object_or_404(Share, id=share_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.share = share
            comment.save()
            return redirect('/', share_id=share.id)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(share=share)
    return render(request, 'core/comment.html', {'form': form, 'share': share, 'comments': comments})


# Share create view
@login_required
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

# Share edit view
@login_required
def edit_share(request, share_id):
    share = get_object_or_404(Share, id=share_id)
    if request.method == 'POST':
        form = ShareForm(request.POST, instance=share)
        if form.is_valid():
            form.save()
            return redirect('stories_detail', share_id=share.id)
    else:
        form = ShareForm(instance=share)
    return render(request, 'core/edit_share.html', {'form': form})

@login_required
def delete_share(request, share_id):    
    share = get_object_or_404(Share, id=share_id)
    if request.user == share.user:
        if request.method == 'POST':
            share.delete()
            messages.success(request, 'Your Share was successfully deleted from NA-Share.')
            return redirect('home')
        return render(request, 'core/delete_share.html', {'share': share})
    else:
        messages.error(request, 'You are not authorized to delete this Share.')
        return redirect('home')
