from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, phone, password, first_name='', last_name='', date_of_birth=None, email=None, address='',points=0):
        """
        Creates and saves a User with the given phone number and pw
        """
        if not phone:
            raise ValueError(_('Phone can not be empty'))
        user = self.model(
            phone = phone,
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            email = self.normalize_email(email),
            address = address,
            points = points
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, first_name='', last_name='', date_of_birth=None, email=None, address='',points=0):
        """
        Creates and saves a Superuser with the given phone and password.
        """

        user = self.create_user(
            phone,
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
            email = self.normalize_email(email),
            address = address,
            points = points,
            password = password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(
        verbose_name = _('Phone Number'),
        max_length = 20,
        unique = True
    )

    first_name = models.CharField(
        verbose_name = _('First Name'),
        max_length = 20,
        blank = True
    )

    last_name = models.CharField(
        verbose_name = _('Last Name'),
        max_length = 20,
        blank = True
    )

    date_of_birth = models.DateField(
        verbose_name = _('Birthday'),
        null = True,
        blank = True
    )

    email = models.EmailField(
        verbose_name = _('Email Address'),
        max_length = 255,
        null = True,
        blank = True
    )

    address = models.TextField(
        verbose_name = _('Address'),
        blank = True
    )

    points = models.PositiveIntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone
