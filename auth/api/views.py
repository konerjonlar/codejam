from rest_framework import mixins, viewsets

from auth.api.serializers import SkillSerializer, SocialSerializer, UserSerializer
from auth.models import Skill, Social, User


class SocialViewSet(viewsets.ModelViewSet):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
