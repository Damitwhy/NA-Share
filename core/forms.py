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

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
class SearchForm(forms.Form):
    query = forms.CharField()
    
    
