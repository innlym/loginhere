# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class HereUserManager(BaseUserManager):
    def create_user(self, username, password, email):
        if not username:
            raise ValueError('An username is required!')
        if not email:
            raise ValueError('An email is required!')
        user = self.model(
            username=username,
            email=HereUserManager.normalize_email(email),
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class HereUser(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
        ('O', '保密'),
    )

    username = models.CharField(max_length=32,unique=True,db_index=True)
    email = models.EmailField(unique=True, max_length = 255)
    #avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    nickname = models.CharField(max_length=32, blank=True)
    realname = models.CharField(max_length=32, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='O')
    mobile = models.CharField(max_length=32, blank=True)
    birthday = models.DateField(null=True, blank=True)
    mydesc = models.TextField(max_length=64, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = HereUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        app_label = 'accounts'

    def get_full_name(self):
        return self.realname

    def get_short_name(self):
        return self.nickname

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin