from rest_framework import serializers
from v0.models import (Log,
    Person,
    Offer, OfferTag, OfferComment
)
#, AgentsFiz, Agent

# class FeedbackSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     phone = serializers.CharField(max_length=20)
#     email = serializers.EmailField()
#     pers_data_accepted = serializers.IntegerField()
#     #content = serializers.CharField(max_length=20000)
#     #created = serializers.DateTimeField()

#     def create(self, validated_data):
#         Log.objects.create(name=validated_data['name'], log_data=validated_data)
#         return validated_data

#     def validate_date(self):
#         if self.pers_data_accepted != 117:
#             raise serializers.ValidationError("Perosnal data agreement is not accepted!")   

# class AgentsFizSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=AgentsFiz
#         fields = '__all__'


# class AgentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Agent
#         fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Log
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
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
