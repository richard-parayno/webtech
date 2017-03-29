from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="password", max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(label="password2", max_length=50, widget=forms.PasswordInput)


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(("The username already exists. Please try again."))

    def clean(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError(("The two password fields did not match."))
        return self.cleaned_data



