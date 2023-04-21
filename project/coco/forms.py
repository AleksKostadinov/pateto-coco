from .models import Comment, Subscribers, MailMessage
from django import forms
# from .utils import is_valid_email


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SubscribersForm(forms.ModelForm):
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address...'})
    )

    class Meta:
        model = Subscribers
        fields = ['email']

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if not is_valid_email(email):
    #         raise forms.ValidationError("Invalid email address")
    #     return email
