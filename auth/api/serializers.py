from rest_framework import serializers

from auth.models import Skill, Social, User


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ("name", "logo", "link")

    def __str__(self) -> str:
        return self.name


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("id","name", "logo", "description")

    def __str__(self) -> str:
        return self.name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("social", "skills")

    def __str__(self) -> str:
        return self.name
