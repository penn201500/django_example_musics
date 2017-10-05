# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Music
from serializers import MusicSerializer
from rest_framework import viewsets

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
    })

def display_musics(request):
    musics = Music.objects.all()
    return render(request, 'display_musics.html', {'musics': musics})
