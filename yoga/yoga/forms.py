from django import forms


class PostureForm(forms.Form):
    name = forms.CharField(label='Name', max_length=128)
    description = forms.CharField(label='Description', max_length=256)
    picture = forms.CharField(label='Picture URL', max_length=256)


class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=64)
    email = forms.CharField(label='Email', max_length=256, widget=forms.EmailInput)
    password = forms.CharField(label='Password', max_length=16, widget=forms.PasswordInput)
