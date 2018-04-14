from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Category, Event


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    categories = StringRelatedField(many=True)

    class Meta:
        model = Event
        fields = '__all__'
