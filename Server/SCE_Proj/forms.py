from django import forms

#login form
class Login(forms.Form):
    user = forms.EmailField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput(),max_length =30)

#register form
class Register(forms.Form):
    name = forms.CharField(max_length =20)
    surname = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput(),max_length = 30)
    confirmpass = forms.CharField(widget = forms.PasswordInput(),max_length = 30)