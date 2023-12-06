from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import MyUser
from django.contrib.auth.forms import PasswordResetForm
from django import forms
from captcha.fields import CaptchaField


class MyUserCreationForm(UserCreationForm):
    captcha = CaptchaField(error_messages={'required': u'验证码不能为空', 'invalid': u'验证码错误'})

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        model = MyUser
        # 在注册界面添加邮箱、手机号码、微信号码和QQ号码
        fields = UserCreationForm.Meta.fields
        fields += ('email', 'mobile', 'weChat', 'qq')
        error_messages = {
            'username': {
                'unique': "Username Exist !!Oh.",
            },
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if MyUser.objects.filter(email=email).exists():
            raise ValidationError("Email Exist")
        return email


class MyPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not MyUser.objects.filter(email=email).exists():
            raise ValidationError('Email not Exist')
        return email


class CaptchaForm(forms.Form):
    captcha = CaptchaField(error_messages={'required': u'验证码不能为空', 'invalid': u'验证码错误'})
