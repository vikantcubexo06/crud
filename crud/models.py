
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser, User
from django.core.validators import RegexValidator
from django.db import models
#
# class UserManager(BaseUserManager):
#
#     def create_user(self, username, password=None, **extra_fields):
#         user= self.model(username=username)
#         user.set_password(password)
#         user.save(using=self.db)
#
#         return user


# class CreateUser(AbstractUser):
#
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=50)
#     contact = models.CharField(max_length=10)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#
#     is_active = True
#     REQUIRED_FIELDS = []


class Information(models.Model):
    User_name = models.ForeignKey(User, on_delete=models.CASCADE, null= False , blank= True)
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Age = models.IntegerField()

    def __str__(self):
        return self.User_name