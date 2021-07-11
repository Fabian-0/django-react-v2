from django.contrib.auth.models import User
from rest_framework.response import Response
from moduls.classes.models import Classroom
from rest_framework.viewsets import ModelViewSet
from moduls.students.serializer import StudentGetSerializer, StudentCreateSerializer
from moduls.students.permissions import StuentPermissions
from rest_framework import status
from rest_framework.decorators import action
from django.core.mail import send_mail
from moduls.students.tasks import student_send_mail

class StudentsViewSet(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = StudentGetSerializer
  permission_classes = (StuentPermissions, )
  pagination_class = None

  def list(self, request, *args, **kwargs):
    serializer = self.get_serializer_class()
    serialized = serializer(request.user)
    return Response(status=status.HTTP_200_OK, data=serialized.data)

  def create(self,  request, *args, **kwargs):
    serialized = StudentCreateSerializer(data=request.data)
    if serialized.is_valid():
      student_send_mail.apply_async(args=[request.data['email']])
      serialized.save()
      return Response(status=status.HTTP_201_CREATED, data={'id': serialized.instance.id})
    return Response(status=status.HTTP_400_BAD_REQUEST)

  @action(methods=['POST','DELETE'], detail=True)
  def classes(self, request, pk):
    if request.method == 'POST':
      queryset = Classroom.objects.get(id=request.data['id'])
      request.user.student.classes.add(queryset)
      return Response(status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
      queryset = Classroom.objects.get(id=pk)
      request.user.student.classes.remove(queryset)
      return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)
