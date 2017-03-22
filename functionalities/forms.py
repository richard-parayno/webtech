from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password1 = forms.CharField(label="password1", max_length=100)
    password2 = forms.CharField(label="password2", max_length=100)

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try again."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

class LogInForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", max_length=100)


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try again."))
