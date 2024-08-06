from django import forms
from django_summernote.widgets import SummernoteWidget
from django.forms import ModelForm
from .models import Comment, Share

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment here!'}),
        }
        
class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }

class ContactForm(forms.Form):    
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)
    
    
class SearchForm(forms.Form):
    query = forms.CharField()
    
    
