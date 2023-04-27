from .models import Comment, Subscribers, MailMessage
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        labels = {
            'body': 'Message'
        }


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


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = ['email', 'title', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Please enter so I can keep in touch with you.'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'What best describes your epic quest?'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Let me know in the field below!'
            })
        }
