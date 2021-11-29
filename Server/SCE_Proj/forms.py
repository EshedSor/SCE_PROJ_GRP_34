from django import forms
from django.contrib.auth.models import User
from SCE_Proj.models import tmp

#login form
class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput(),max_length =30)
    class Meta:
        model = tmp
        fields = ('email')
    def clean_email(self):
        emailval = self.cleaned_data.get('email')
        dbuser = tmp.objects.get(email = emailval)
        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")        
        return emailval
#register form
class RegisterForm(forms.Form):

    name = forms.CharField(max_length =20)
    surname = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput(),max_length = 30)
    confirmpass = forms.CharField(widget = forms.PasswordInput(),max_length = 30)
