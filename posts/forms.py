from django.contrib.auth.models import User
from django import forms
from .forms import User
from .models import Comment, Post, Categories


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', ]




class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text',  'created_at', ]


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "category",
            "post_title",
            "post_body",
            "image",
            "post_date",
        ]


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "category",
            "post_title",
            "post_body",
            "image",
            "post_date",
        ]

