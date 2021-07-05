from django.db import models
from moduls.GenericUser.models import CommonUser
# Create your models here.

class Professor(CommonUser):
  qualification = models.CharField(max_length=150, null=True,)