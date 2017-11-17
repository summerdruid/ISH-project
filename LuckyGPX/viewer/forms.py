from django import forms
from viewer.models import Point, Run, Route, UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UploadFileForm(forms.Form):
    route = forms.ChoiceField(choices=(), required=True)
    file = forms.FileField()
