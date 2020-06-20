from rest_framework import serializers
from v0.models import (Log,
    Offer, OfferTag, OfferComment
)

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Log
        fields = '__all__'


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model=Offer
        fields = '__all__'

class OfferTagSerializer(serializers.ModelSerializer):
    class Meta:
        model=OfferTag
        fields = '__all__'

class OfferCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=OfferComment
        fields = '__all__'
