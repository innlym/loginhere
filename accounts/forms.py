# -*- coding: utf-8 -*-
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from models import HereUser

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = HereUser
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("密码不匹配！")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if (not user.nickname) or user.nickname=='':
            user.nickname = user.username
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(help_text=
        "Raw passwords are not stored, so there is no way to see "
        "this user's password, but you can change the password "
        "using <a href=\"password/\">this form</a>."
    )
    

    class Meta:
        model = HereUser

    def clean_password(self):
        return self.initial['password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = HereUser
        fields = ('nickname', 'realname', 'gender', 'mobile', 'birthday', 'mydesc')
        labels = {
            'nickname': '昵称',
            'realname': '真实姓名',
            'gender': '性别',
            'mobile': '手机',
            'birthday': '生日',
            'mydesc': '个人简介',
        }


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


