from django import forms

class UserRegistration(forms.Form):
    first_name = forms.CharField(label='First Name',label_suffix='')
    last_name = forms.CharField(label='Last Name',label_suffix='')
    email = forms.EmailField(label_suffix='')
    nid = forms.IntegerField(label='NID',label_suffix='')
    laptop = forms.CharField(widget=forms.HiddenInput())
    bio = forms.CharField(widget=forms.Textarea())