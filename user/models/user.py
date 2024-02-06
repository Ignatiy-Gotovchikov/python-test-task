from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, verbose_name='Username', unique=True)
    password = models.CharField(max_length=255, verbose_name='Password')
    email = models.EmailField(max_length=255, verbose_name='Email', unique=True)
    first_name = models.CharField(max_length=255, verbose_name="first name")
    last_name = models.CharField(max_length=255, verbose_name="last name", null=True, blank=True)
    is_staff = models.BooleanField(verbose_name="staff status", default=False)
    is_active = models.BooleanField(verbose_name="active", default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.pk}"

    def save(self, *args, **kwargs):
        """Save method, for hashing password."""
        if self._state.adding:  # Checking if the object is being created
            self.set_password(self.password)
        super().save(*args, **kwargs)
