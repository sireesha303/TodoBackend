"""
Models for todoapp
"""
from django.contrib.auth.models import User
from django.db import models


# class User(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(max_length=200, null=False, blank=True, unique=True)
#     username = models.CharField(max_length=255, unique=True)
#
#     def __str__(self):
#         """String representation of the User model"""
#         return self.email


def get_default_user():
    """"
    get_default_user
    """
    return User.objects.get(username="sireesha")


class Todo(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=get_default_user)

    def __str__(self):
        """String representation of the Todo model"""
        return self.title
