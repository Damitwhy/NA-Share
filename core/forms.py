from django import forms
from django_summernote.widgets import SummernoteWidget
from django.forms import ModelForm
from .models import Comment, Share

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'rating']
        
class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }
