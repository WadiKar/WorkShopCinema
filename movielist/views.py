# from movielist.forms import MovieAddForm
from movielist.models import Movie, Person
from movielist.serializers import MovieSerializer, PersonSerializer
from rest_framework import generics
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import render


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



