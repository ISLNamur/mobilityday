from rest_framework import serializers

from .models import StudentMobilityModel, SchoolMobilityModel


class SchoolMobilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolMobilityModel
        fields = "__all__"


class StudentMobilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMobilityModel
        fields = "__all__"
