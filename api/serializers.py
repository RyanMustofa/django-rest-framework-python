from rest_framework import serializers
from .models import Lists

class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lists
        fields = '__all__'
