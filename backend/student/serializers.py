from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['stuid', 'name', 'email', 'password', 'phone', 'address', 'gender', 'profile_pic']