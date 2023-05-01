from rest_framework import serializers
from .models import Users, Client, Project


class UserSerializers(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField

    class Meta:
        model = Users
        fields = "__all__"


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Client
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = '__all__'
