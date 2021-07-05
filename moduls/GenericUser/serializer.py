from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class CommonSerializer(ModelSerializer):
  
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name', 'last_name', )

class CommonCreateSerializer(ModelSerializer):
  
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password' ) 