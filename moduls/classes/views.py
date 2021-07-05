from django.shortcuts import render
from moduls.classes.models import Classroom
from moduls.classes.serializer import ClassroomSerializer, ClassroomCreateSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from moduls.classes.permissions import ClassroomPermissions

class ClasseroomViewSet(ModelViewSet):
  queryset = Classroom.objects.all().order_by('id')
  serializer_class = ClassroomSerializer
  permission_classes = (ClassroomPermissions, )

  def create(self, request, *args, **kwargs):
    createClass = {
      "professor": request.user.id,
      "name": request.data["name"]
    }
    serializer = ClassroomCreateSerializer(data=createClass)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED)
    print(serializer.is_valid())
    return Response(status=status.HTTP_400_BAD_REQUEST)

  def update(self, request, *args, **kwargs):
    classObject = self.get_queryset().filter(id=request.parser_context['kwargs']['pk'])

    if not classObject.exists():
      return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.data['professor'] != request.user.id:
      return Response(status=status.HTTP_400_BAD_REQUEST)

    classObject.update(name=(request.data['name']))

    return Response(status=status.HTTP_200_OK)