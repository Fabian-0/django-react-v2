from django.shortcuts import render
from moduls.classes.models import Classroom
from moduls.classes.serializer import ClassroomSerializer, ClassroomCreateSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from moduls.classes.permissions import ClassroomPermissions

class ClasseroomViewSet(ModelViewSet):
  queryset = Classroom.objects.all().order_by('id')
  serializer_class = ClassroomSerializer
  permission_classes = (ClassroomPermissions, )
  custom_validations = [None, '']

  def create(self, request, *args, **kwargs):

    if request.data.get('name') in self.custom_validations:
      return Response(status=status.HTTP_400_BAD_REQUEST)
    createClass = {
      "professor": request.user.id,
      "name": request.data["name"]
    }
    serializer = ClassroomCreateSerializer(data=createClass)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED, data={'id': serializer.instance.id})

    return Response(status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, *args, **kwargs):
    
    classObject = self.get_object()
    if request.data.get('name') in self.custom_validations:
      return Response(status=status.HTTP_400_BAD_REQUEST)
    classObject.name = request.data['name']
    classObject.save()

    return Response(status=status.HTTP_200_OK)

  def destroy(self, request, *args, **kwargs):
    to_delete = self.get_object()
    
    if to_delete.professor_id != request.user.id:
      return Response(status=status.HTTP_403_FORBIDDEN)
  
    to_delete.delete()
  
    return Response(status=status.HTTP_204_NO_CONTENT) 