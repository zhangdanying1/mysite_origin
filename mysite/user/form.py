from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import MyUser
from django.contrib.auth.forms import PasswordChangeForm


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        model = MyUser
        # 在注册界面添加邮箱、手机号码、微信号码和QQ号码
        fields = UserCreationForm.Meta.fields
        fields += ('email', 'mobile', 'weChat', 'qq')

    def clean_email(self):
        email = self.cleaned_data['email']
        if MyUser.objects.filter(email=email).exists():
            raise ValidationError("Email Exist")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if MyUser.objects.filter(username=username).exists():
            raise ValidationError("Username Exist")
        return username


class MyPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        new_password1 = self.cleaned_data['new_password1']
        if self.user.check_password(new_password1):
            raise ValidationError("New password cannot be the same as the old one")
        return new_password1
