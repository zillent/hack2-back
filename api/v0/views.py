from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS
from v0.models import (
    Log,
    Offer, OfferTag, OfferComment
)
from v0.serializers import (
    LogSerializer,
    OfferSerializer, OfferTagSerializer, OfferCommentSerializer
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

class OfferView(ListCreateAPIView):
    queryset=Offer.objects.all().order_by('-id')
    serializer_class = OfferSerializer

class SingleOfferView(RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer