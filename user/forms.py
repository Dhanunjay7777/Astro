from django import forms
from .models import register, Feedback, Contact


class registerForm(forms.ModelForm):
    class Meta:
        model = register
        fields = "__all__"
        exclude = {"registrationtime"}
        labels = {"name": "FullName", "gender": "Gender", "email": "Email", "contact": "Phone Number"}
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'query']

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model=Contact
#         fields="__all__"
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label='Firstname')
    last_name = forms.CharField(max_length=50, required=True, label='Lastname')
    email = forms.EmailField(required=True, label='Email')
    need = forms.ChoiceField(
        choices=[
            ('', '--Select Your Issue--'),
            ("Couldn't get sign", "Couldn't get sign"),
            ("Request horoscope report", "Request horoscope report"),
            ("Couldn't get prediction/option", "Couldn't get prediction/option"),
            ("Other", "Other"),
        ],
        required=True,
        label='Issue '
    )
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message ')