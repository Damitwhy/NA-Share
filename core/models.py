from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Share(models.Model):
    """
    Model representing a share.
    Attributes:
        user (User): The user who created the share.
        title (str): The title of the share.
        content (str): The content of the share.
        created_at (datetime): The date and time when the share was created.
        updated_at (datetime): The date and time when the share was last updated.
        status (str): The status of the share. Can be one of 'pending', 'approved', or 'rejected'.
        average_rating (int): The average rating of the share.
    Methods:
        __str__(): Returns a string representation of the share.
    """
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shares')
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    average_rating = models.IntegerField(default=0)
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"Title: {self.title} | Written by: {self.user}"
    

class Comment(models.Model):
    """
    Model representing a comment.
    Attributes:
        share (Share): The share associated with the comment.
        user (User): The user who made the comment.
        parent (Comment, optional): The parent comment if this is a reply.
        content (str): The content of the comment.
        rating (int, optional): The rating given to the comment.
        created_at (datetime): The date and time when the comment was created.
        updated_at (datetime): The date and time when the comment was last updated.
        approved (bool): Indicates if the comment has been approved.
    """
    share = models.ForeignKey(Share, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    content = models.TextField()
    rating = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment {self.content} by {self.user}"
    

class Message(models.Model):
    """
    Represents a message sent between users.
    Attributes:
        sender (User): The user who sent the message.
        sender_email (str): The email address of the sender (optional).
        receiver (User): The user who received the message.
        content (str): The content of the message.
        created_at (datetime): The date and time when the message was created.
        is_read (bool): Indicates whether the message has been read or not.
    """
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.SET_NULL, null=True, blank=True)
    sender_email = models.EmailField(blank=True, null=True)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Rating(models.Model):
    share = models.ForeignKey(Share, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_value = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class ServiceLink(models.Model):
    url = models.URLField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
