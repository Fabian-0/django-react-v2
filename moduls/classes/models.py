from django.db import models
from django.contrib.auth.models import User
from moduls.GenericUser.models import CommonUser
# Create your models here.

class Classroom(models.Model):
  professor = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)