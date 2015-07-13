from django import forms
from django.contrib.auth.models import User
from article.models import Article


class UserForm(forms.ModelForm):
    # username = forms.CharField(label="username", max_length=100)
    # password = forms.CharField(label="password", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ('title', 'content',)
