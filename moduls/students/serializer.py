from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from moduls.GenericUser.serializer import CommonSerializer, CommonCreateSerializer
from moduls.students.models import Student
from moduls.classes.serializer import ClassroomSerializer

# Get serializers

class StudentAuxSerializer(ModelSerializer):

  classes = ClassroomSerializer(many=True)

  class Meta:
    model = Student
    fields = ('classes', 'avatar' )

class StudentGetSerializer(CommonSerializer):

  student = StudentAuxSerializer()

  class Meta(CommonSerializer.Meta):
    model = User
    fields = CommonSerializer.Meta.fields + ('student', )

# Create serializeres

class StudentAuxCreateSerializer(ModelSerializer):

  class Meta:
    model = Student
    fields = ('phone_number', 'avatar', 'gender', )

class StudentCreateSerializer(CommonCreateSerializer):

  student = StudentAuxCreateSerializer()

  class Meta(CommonCreateSerializer.Meta):
    fields = CommonCreateSerializer.Meta.fields + ('student', )

  def create(self, validated_data):
    profile_data = validated_data.pop('student')
    user = User.objects.create(**validated_data)
    user.set_password(validated_data['password'])
    student = Student.objects.create(user=user, **profile_data)
    user.save()
    return user