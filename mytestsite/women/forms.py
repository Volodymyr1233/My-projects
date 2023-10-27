from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=300, label='Заголовок', widget=forms.TextInput(attrs={'class': 'title_field'}))
    slug = forms.SlugField(max_length=200, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 30}), label='вміст')
    is_published = forms.BooleanField(label='Стан публікації')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Виберіть категорію')