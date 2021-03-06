from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Programmer, Paradigm
from .serializers import LanguageSerializers, ParadigmSerializer, ProgrammerSerializers

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializers
