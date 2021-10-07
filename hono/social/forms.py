from django import forms
from .models import Post,Comment,MessageModel, Tag, UserProfile

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2',
            'cols': '25',
            'placeholder': 'Caption'
        })
    )
    image = forms.ImageField(
        required=False,
        widget= forms.ClearableFileInput(attrs={
            'multiple': True
        })
    )
    class Meta:
        model = Post
        fields = ['body']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say something!'
        })
    )
    class Meta:
        model = Comment
        fields = ['comment']

class ThreadForm(forms.Form):
    username= forms.CharField(label='',max_length=100)

class MessageForm(forms.ModelForm):
    body = forms.CharField(label='',max_length=1000)

    image = forms.ImageField(required=False)
    class Meta:
        model = MessageModel
        fields = ['body','image']

class SharedForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say something!'
        })
    )
    

class ExploreForm(forms.Form):
    query = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            'placeholder': 'Explore Tags'
        })
    )