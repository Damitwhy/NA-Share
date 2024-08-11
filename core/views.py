from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
# from .models import Post
from .models import Share, Comment, Message, User, Rating, ContactMessage, VisitorCount
from .forms import CommentForm, ShareForm, ContactForm
from django.contrib import messages


# Create your views here.

class ShareListView(ListView):
    model = Share
    template_name = 'core/home.html'
    context_object_name = 'shares'
    paginate_by = 3  # Number of shares per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Visitor count logic
        visitor_count, created = VisitorCount.objects.get_or_create(id=1)
        visitor_count.count += 1
        visitor_count.save()
        
        # Add visitor count to context
        context['visitor_count'] = visitor_count.count
        
        # Example: Count the number of shares
        context['count'] = Share.objects.count()
        
        # User-specific shares
        context['user_shares'] = Share.objects.filter(user=self.request.user) if self.request.user.is_authenticated else []
        
        return context
    
    
def get_average_rating_for_share(share_id):
    """
    Returns the average rating for a specific share.
    """
    average_rating = Rating.objects.filter(share_id=share_id).aggregate(Avg('score'))['score__avg']
    return average_rating


def about(request):
    """
    Renders the 'about.html' template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - The rendered 'about.html' template.
    """
    return render(request, 'core/about.html')
 
 
def contact(request):
    """
    View function for the contact page.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The HTTP response object.
    Raises:
        None
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle the form data here
            form.save()
            messages.success(request, 'Your message was successfully sent.')
            return redirect('/')  # Replace 'success' with the appropriate URL for the success template
    else:
        
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


def services(request):
    """
    Render the 'services.html' template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - The rendered 'services.html' template.
    """
    return render(request, 'core/services.html')


def home(request):
    """
    Renders the home page.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - A rendered HTML response containing the home page.
    """
    
    visitor_count, created = VisitorCount.objects.get_or_create(id=1)    
    visitor_count.count += 1    
    visitor_count.save()    
    shares = Share.objects.all()
    user_shares = Share.objects.filter(user=request.user) if request.user.is_authenticated else []    
    return render(request, 'core/home.html', {'shares': shares, 'user_shares': user_shares, 'visitor_count': visitor_count.count})


def stories_detail(request, share_id):
    """
    View function for displaying the details of a story.

    Args:
        request (HttpRequest): The HTTP request object.
        share_id (int): The ID of the share.

    Returns:
        HttpResponse: The HTTP response object containing the rendered HTML template.
    """
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
    """
    Handles the creation of comments for a specific share.

    Parameters:
    - request: The HTTP request object.
    - share_id: The ID of the share for which the comment is being created.
    - parent_id: (optional) The ID of the parent comment, if this comment is a reply.

    Returns:
    - If the request method is POST and the form is valid, redirects to the 'stories_detail' view for the share.
    - Otherwise, renders the 'core/comment.html' template with the comment form, share, comments, and parent comment.

    Note:
    - This function assumes the existence of the Share and Comment models.
    - The comment form is initialized with the initial content and is_reply parameters.
    - Comments are ordered by creation date in descending order.
    """
    share = get_object_or_404(Share, id=share_id)
    parent_comment = get_object_or_404(Comment, id=parent_id) if parent_id else None
    initial_content = f"@{parent_comment.user.username} " if parent_comment else ''
    is_reply = parent_comment is not None

    if request.method == 'POST':
        form = CommentForm(request.POST, initial_content=initial_content, is_reply=is_reply)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.share = share
            if parent_comment:
                comment.parent = parent_comment
            comment.save()
            return redirect('stories_detail', share_id=share.id)
    else:
        form = CommentForm(initial_content=initial_content, is_reply=is_reply)
        # Order comments by creation date in descending order
        comments = Comment.objects.filter(share=share).order_by('-created_at')

    return render(request, 'core/comment.html', {'form': form, 'share': share, 'comments': comments, 'parent_comment': parent_comment})


@login_required
def edit_comment(request, share_id, comment_id):
    """
    Edit a comment.

    Args:
        request (HttpRequest): The HTTP request object.
        share_id (int): The ID of the share.
        comment_id (int): The ID of the comment.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        Http404: If the comment with the given ID does not exist.
    """
    ...
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
    """
    Reply to a comment.

    Args:
        request (HttpRequest): The HTTP request object.
        share_id (int): The ID of the share.
        parent_id (int): The ID of the parent comment.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        Http404: If the parent comment does not exist.

    """
    ...
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
    """
    Delete a comment.

    Args:
        request (HttpRequest): The request object.
        share_id (int): The ID of the share.
        comment_id (int): The ID of the comment to be deleted.

    Returns:
        HttpResponseRedirect: A redirect to the 'stories_detail' view.

    Raises:
        Http404: If the comment with the given ID does not exist.

    """
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
    """
    Create a new share.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        None

    """
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
    """
    Edit a share.

    Args:
        request (HttpRequest): The HTTP request object.
        share_id (int): The ID of the share to be edited.

    Returns:
        HttpResponse: The HTTP response object.

    Raises:
        Http404: If the share with the given ID does not exist.

    """
    share = get_object_or_404(Share, id=share_id)
    if request.user == share.user:
        if request.method == 'POST':
            form = ShareForm(request.POST, instance=share)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Share was successfully updated.')
                return redirect('stories_detail', share_id=share.id)
        else:
            form = ShareForm(instance=share)
        return render(request, 'core/edit_share.html', {'form': form})
    else:
        messages.error(request, 'You are not authorized to edit this Share.')
        return redirect('home')
    
# Share delete view
@login_required
def delete_share(request, share_id):   
    """
    Delete a share.

    Args:
        request (HttpRequest): The HTTP request object.
        share_id (int): The ID of the share to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the home page after successful deletion.

    Raises:
        Http404: If the share with the given ID does not exist.

    Notes:
        - Only the user who created the share can delete it.
        - If the request method is not POST, the delete_share.html template is rendered.
        - If the user is not authorized to delete the share, an error message is displayed and the user is redirected to the home page.
    """
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


