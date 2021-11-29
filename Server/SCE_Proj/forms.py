from django import forms

#login form
class Login(forms.Form):
    user = forms.CharField(max_length = models.User.name.max_length)
    password = forms.CharField(widget = forms.PasswordInput(),max_length = models.User.password.max_length)

#register form
class Register(forms.Form):
    user = forms.CharField(max_length = models.User.name.max_length)
    password = forms.CharField(widget = forms.PasswordInput(),max_length = models.User.password.max_length)
