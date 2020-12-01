from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from Collection.models import Collection


class MyAccountManager(BaseUserManager):
    def create_user(self, username, password):
        user = self.model(username=username)
        user.set_password(password)
        user.is_active = True
        user.date_joined = datetime.datetime.today()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    """
    This Table will hold the data about the users
    """
    # full name of the user
    username = models.CharField(max_length=30, null=True, unique=True)

    # alphanumeric password field
    password = models.CharField(max_length=100, null=False)

    is_admin = models.BooleanField(default=False)

    is_active = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(verbose_name='date joined')

    collections = models.ManyToManyField(Collection, related_name='collections', blank=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
