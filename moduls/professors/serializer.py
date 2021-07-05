from django.contrib.auth.models import User
from moduls.professors.models import Professor
from moduls.classes.serializer import ClassroomSerializer
from moduls.classes.serializer import ClassroomSerializer
from moduls.GenericUser.serializer import CommonSerializer, CommonCreateSerializer

class ProfessorAuxSerializer(CommonSerializer):

  class Meta:
    model = Professor
    fields =  ('qualification', 'avatar', )


class ProfessorSerializer(CommonSerializer):

  professor = ProfessorAuxSerializer()
  classroom_set = ClassroomSerializer(many=True, )

  class Meta(CommonSerializer.Meta):
    fields = CommonSerializer.Meta.fields + ('professor', 'classroom_set' )


class ProfessorAuxCreateSerializer(CommonSerializer):

  class Meta:
    model = Professor
    fields =  ('qualification', 'avatar', 'phone_number', 'gender', )

class ProfessorCreateSerializer(CommonCreateSerializer):

  professor = ProfessorAuxCreateSerializer()

  class Meta(CommonCreateSerializer.Meta):
    fields = CommonCreateSerializer.Meta.fields + ('professor', )

  def create(self, validated_data):
    profile_data = validated_data.pop('professor')
    user = User.objects.create(**validated_data)
    user.set_password(validated_data['password'])
    professor = Professor.objects.create(user=user, **profile_data)
    user.save()
    return user