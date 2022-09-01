from rest_framework import serializers
from .models import Position, Employee



class PositionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Position.objects.create(**validated_data)



class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    birth_date = serializers.DateField()
    salary = serializers.IntegerField()
    position = PositionSerializer()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
