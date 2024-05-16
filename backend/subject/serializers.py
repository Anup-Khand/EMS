from rest_framework import serializers
from .models import subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = ['subid', 'name']