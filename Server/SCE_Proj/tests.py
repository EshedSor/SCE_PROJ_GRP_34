from django.test import TestCase
from SCE_Proj.forms import loginForm,RegisterForm
from SCE_Proj.views import search_feature
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
# Create your tests here.


#unittesting for the login form
class LoginFormTestCase(TestCase):
    def test_LoginForm_is_valid(self):
        #valid form
        valid_email  = loginForm(data = {"email":"exmaple@example.com","password":"1"})
        valid_pass  = loginForm(data = {"email":"a@example.com","password":"123123"})
        invalid_form  = loginForm(data = {"email":"a@example.com","password":"1a23123"})
        self.assertFalse(valid_pass.is_valid())
        self.assertFalse(valid_pass.is_valid())
        self.assertFalse(invalid_form.is_valid())

class RegisterFormTestCase(TestCase):
    def test_RegisterForm_is_valid(self):
        #valid form
        random_mail = "{0}@{0}.com".format(id_generator())
        random_pass = id_generator()
        random_name = id_generator()
        random_surname = id_generator()
        valid_form = RegisterForm(data = {'name':random_name,'surname':random_surname,'email':random_mail,'password':random_pass,'confirmpass':random_pass})
        #passwords dont match
        random_mail = "{0}@{0}.com".format(id_generator())
        random_pass = id_generator()
        random_name = id_generator()
        random_surname = id_generator()
        pass_form = RegisterForm(data = {'name':random_name,'surname':random_surname,'email':random_mail,'password':random_pass,'confirmpass':"1"})
        #an existing user
        email = "example@example.com"
        exist_form =  RegisterForm(data = {'name':random_name,'surname':random_surname,'email':email,'password':random_pass,'confirmpass':"1"})
        self.assertTrue(valid_form.is_valid())
        self.assertFalse(pass_form.is_valid())
        self.assertFalse(exist_form.is_valid())

        
class SearchFeatureTestCase(TestCase):
    def test_search_feature(self):
        pass
