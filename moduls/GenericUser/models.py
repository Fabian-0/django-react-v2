from django.db import models
from django.contrib.auth.models import User

CHOICES = [
  ('female', 'F'),
  ('male', 'M'),
  ('other', 'O')
]

class CommonUser(models.Model):
  user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=15, null=True)
  avatar = models.URLField(max_length=255, null=True)
  gender = models.CharField(max_length=6, choices=CHOICES, null=True)

  class Meta:
    abstract = True
  
