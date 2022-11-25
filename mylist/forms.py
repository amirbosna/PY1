from django import forms
from .models import Post, Comment

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'beschreibung', 'public', 'link', 'author')
        labels = {'name': ('Titel'), 'beschreibung': ('Beschreibung'), 'public': ('Sichtbarkeit'), 'link': ('Tags'), 'author': ('')}

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'beschreibung':forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'public':forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'link':forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'author':forms.TextInput(attrs={'class': 'hidden', 'autocomplete': 'off'}),
        }



class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Kommentar',
        'rows': '2',
        'style':'resize:none; border-color: #76c2f8',
    }), label=False)

    class Meta:
        model = Comment
        fields = ('content', )