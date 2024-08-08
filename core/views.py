from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
# from .models import Post
from .models import Share, Comment, Message, User, Rating, ContactMessage
from .forms import CommentForm, ShareForm, ContactForm
from django.contrib import messages


# Create your views here.

def get_average_rating_for_share(share_id):
    """
    Returns the average rating for a specific share.
    """
    average_rating = Rating.objects.filter(share_id=share_id).aggregate(Avg('score'))['score__avg']
    return average_rating


def about(request):
    return render(request, 'core/about.html')

 
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle the form data here
            messages.success(request, 'Your message was successfully sent.')
            return redirect('/')  # Replace 'success' with the appropriate URL for the success template
    else:
        messages.error(request, 'There was an error with your message.')
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def services(request):
    return render(request, 'core/services.html')


def home(request):
    shares = Share.objects.all()
    user_shares = Share.objects.filter(user=request.user) if request.user.is_authenticated else []
    for share in shares:
        comment_count = Comment.objects.filter(share=share).count()
    return render(request, 'core/home.html', {'shares': shares, 'user_shares': user_shares, 'comment_count': comment_count})


def stories_detail(request, share_id):
    share = get_object_or_404(Share, id=share_id)
    comments = Comment.objects.filter(share=share)
    comment_count = Comment.objects.filter(share=share).count()
    context = {
        'share': share,
        'comments': comments,
        'comment_count': comment_count,
    }
    
    
    return render(request, 'core/stories_detail.html', context)

# Comment view 

def comment(request, share_id, parent_id=None):
    share = get_object_or_404(Share, id=share_id)
    parent_comment = get_object_or_404(Comment, id=parent_id) if parent_id else None
    context = {
        'share': share,
        'parent_comment': parent_comment,
    }        
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.share = share
            comment.save()
            return redirect('stories_detail', share_id=share.id)
    else:
        form = CommentForm()
    comments = Comment.objects.filter(share=share)
    return render(request, 'core/comment.html', {'form': form, 'share': share, 'comments': comments, 'parent_comment': parent_comment})


@login_required
def edit_comment(request, share_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment was successfully updated.')
            return redirect('stories_detail', share_id=share_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'core/edit_comment.html', {'form': form, 'comment': comment, 'share_id': share_id})


def reply_comment(request, share_id, parent_id):
    parent_comment = get_object_or_404(Comment, id=parent_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.share = parent_comment.share
            reply.parent = parent_comment
            reply.save()
            messages.success(request, 'Your reply was successfully added.')
            return redirect('stories_detail', share_id=share_id)
    else:
        form = CommentForm()
        
    return render(request, 'core/comment.html', {'form': form, 'share': parent_comment.share, 'parent_comment': parent_comment})


@login_required
def delete_comment(request, share_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, 'Your comment was successfully deleted.')
    else:
        messages.error(request, 'You are not authorized to delete this comment.')
    return redirect('stories_detail', share_id=share_id)


# Share create view
@login_required
def create_share(request):
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            share = form.save(commit=False)
            share.user = request.user
            share.save()
            messages.success(request, 'Your Share was successfully created.')
            return redirect('home')
    else:
        form = ShareForm()
    return render(request, 'core/create_share.html', {'form': form})

# Share edit view
@login_required
def edit_share(request, share_id):
    share = get_object_or_404(Share, id=share_id)
    if request.user == share.user:
        if request.method == 'POST':
            form = ShareForm(request.POST, instance=share)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Share was successfully updated.')
                return redirect('/', share_id=share.id)
        else:
            form = ShareForm(instance=share)
        return render(request, 'core/edit_share.html', {'form': form})
    else:
        messages.error(request, 'You are not authorized to edit this Share.')
        return redirect('home')
    
# Share delete view
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


