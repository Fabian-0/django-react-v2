from rest_framework.serializers import Serializer, ModelSerializer
from moduls.classes.models import Classroom
# from moduls.professors.serializer import ProfessorSerializer


class ClassroomCreateSerializer(ModelSerializer):

  class Meta:
    model = Classroom
    fields = ('professor', 'name', )

class ClassroomSerializer(ModelSerializer):

  class Meta:
    model = Classroom
    fields = ('id', 'name', )
