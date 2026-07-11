from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Contact
        fields = "__all__"