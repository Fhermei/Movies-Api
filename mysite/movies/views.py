from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MoviedataSerializer
from .models import Moviedata

# Create your views here.
class MoviedataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MoviedataSerializer

class ActiondataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MoviedataSerializer

class AdventuredataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='adventure')
    serializer_class = MoviedataSerializer

class ComedydataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = MoviedataSerializer

class ChildrendataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='children')
    serializer_class = MoviedataSerializer

class CrimedataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='crime')
    serializer_class = MoviedataSerializer

class RomancedataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='romance')
    serializer_class = MoviedataSerializer

class DramadataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='drama')
    serializer_class = MoviedataSerializer

class AnimationdataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='animation')
    serializer_class = MoviedataSerializer

class HistorydataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='history')
    serializer_class = MoviedataSerializer

class MysterydataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='mystery')
    serializer_class = MoviedataSerializer

class WardataViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='war')
    serializer_class = MoviedataSerializer

