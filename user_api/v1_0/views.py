from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS
from v1_0.models import (
    Log, Person
)
from v1_0.serializers import (
    LogSerializer,
    PersonSerializer,
)

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

# Create your views here.

class LogView(ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
#    def perform_create(self, serializer):
#        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
#        return serializer.save(author=author)


class PersonView(ListCreateAPIView):
    queryset=Person.objects.all()
    serializer_class = PersonSerializer

class SinglePersonView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
