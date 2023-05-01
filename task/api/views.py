from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Users, Client, Project
from .serializers import UserSerializers, ClientSerializer, ProjectSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers



class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer





class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ClientSerializer
