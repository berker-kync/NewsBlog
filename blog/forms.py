from django import forms
from .models import Comment
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),          
        }






    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith('@example.com'):
    #         raise ValidationError("Please use a valid email address with the correct domain.")
    #     return email

