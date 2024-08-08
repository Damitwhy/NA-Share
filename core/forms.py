from django import forms
from django_summernote.widgets import SummernoteWidget
from django.forms import ModelForm
from .models import Comment, Share, ContactMessage
 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment here!', 'rows': 5, 'cols': 50, 'class': 'form-control'}),
        }
        labels = {
            'content': '',
        }

    def __init__(self, *args, **kwargs):
        initial_content = kwargs.pop('initial_content', '')
        is_reply = kwargs.pop('is_reply', False)
        super().__init__(*args, **kwargs)
        if is_reply:
            self.fields['content'].initial = initial_content
        
        
class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        
        labels = {
            'name': '',
            'email': '',
            'message': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message here!', 'rows': 5, 'cols': 15, 'class': 'form-control'}),
        }


class SearchForm(forms.Form):
    query = forms.CharField()
    
    
