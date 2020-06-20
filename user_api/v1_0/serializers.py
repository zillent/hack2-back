from rest_framework import serializers
from v1_0.models import (Log,
    Person, Department
)

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Log
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields = '__all__'
