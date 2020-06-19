from rest_framework import serializers
from api.models import Log, AgentsFiz, Agent

class FeedbackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    pers_data_accepted = serializers.IntegerField()
    #content = serializers.CharField(max_length=20000)
    #created = serializers.DateTimeField()

    def create(self, validated_data):
        Log.objects.create(name=validated_data['name'], log_data=validated_data)
        return validated_data

    def validate_date(self):
        if self.pers_data_accepted != 117:
            raise serializers.ValidationError("Perosnal data agreement is not accepted!")   

class AgentsFizSerializer(serializers.ModelSerializer):
    class Meta:
        model=AgentsFiz
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agent
        fields = '__all__'
