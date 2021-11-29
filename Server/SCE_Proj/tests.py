from django.test import TestCase
from SCE_Proj.forms import LoginForm
# Create your tests here.


#unittesting for the bloguser model
class LoginFormTestCase(TestCase):
    def test_LoginForm_is_valid(self):
        #valid form
        valid_email  = LoginForm(data = {"email":"exmaple@example.com","password":"1"})
        valid_pass  = LoginForm(data = {"email":"a@example.com","password":"123123"})
        invalid_form  = LoginForm(data = {"email":"a@example.com","password":"1a23123"})
        self.assertFalse(valid_pass.is_valid())
        self.assertFalse(valid_pass.is_valid())
        self.assertFalse(invalid_form.is_valid())


