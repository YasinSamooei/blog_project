from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "email-input", "placeholder": "enter your first name"}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "email-input", "placeholder": "enter your last name"}
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "email-input", "placeholder": "enter your email"}
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "email-input", "placeholder": "enter your text"}
        )
    )

    class Meta:
        model = Contact
        fields = ("name", "last_name", "email", "content")
