from django.contrib.auth.models import User
from rest_framework import response, status
from rest_framework.viewsets import ModelViewSet
from moduls.professors.serializer import ProfessorCreateSerializer, ProfessorSerializer
from rest_framework.decorators import action
from moduls.professors.permissions import ProfessorPermissions

# Create your views here.

class ProfessorsViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = ProfessorSerializer
  permission_classes =  [ProfessorPermissions]

  def list(self, request, *args, **kwargs):
    serializer = self.get_serializer_class()
    serialized = serializer(request.user)
    return response.Response(status=status.HTTP_200_OK, data=serialized.data)

  def create(self, request, *args, **kwargs):
    user = ProfessorCreateSerializer(data=request.data)
    if not user.is_valid():
      return response.Response(status=status.HTTP_400_BAD_REQUEST)
    user.save()
    return response.Response(status=status.HTTP_201_CREATED, data={'id': user.instance.id}) 
    