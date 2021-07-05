from django.db import models
from moduls.GenericUser.models import CommonUser
from moduls.classes.models import Classroom
# Create your models here.

class Student(CommonUser):
  classes = models.ManyToManyField(Classroom, )