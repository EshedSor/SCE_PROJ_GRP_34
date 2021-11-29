from django import forms
from django.contrib.auth.models import User
from SCE_Proj.models import bloguser

#login form
class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput(),max_length =30)
    class Meta:
        model = bloguser
    #email validation
    def clean_email(self):
        emailval = self.cleaned_data.get('email')
        #querying the database
        try:
            dbemail = bloguser.objects.get(email = emailval)
        except bloguser.DoesNotExist:
            raise forms.ValidationError("User does not exist in our db!")        
        return emailval
    #password validation
    def clean_password(self):
        passval = self.cleaned_data.get('password')
        #querying the database
        try:
            dbpass = bloguser.objects.get(password = passval)
        except bloguser.DoesNotExist:
            raise forms.ValidationError("User does not exist in our db!")        
        return passval
#register form
class RegisterForm(forms.Form):
    name = forms.CharField(max_length =20)
    surname = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput(),max_length = 30)
    confirmpass = forms.CharField(widget = forms.PasswordInput(),max_length = 30)
    class Meta:
        model = bloguser
    #email validation
    def clean_email(self):
        emailval = self.cleaned_data.get('password')
        #querying the database
        if not bloguser.objects.filter(email = emailval).exists():
            return emailval
        return False
        
    def clean_password(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirmpass'):
            return False
        return self.cleaned_data.get('password')
    