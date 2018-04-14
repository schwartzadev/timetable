from rest_framework import viewsets
from .models import Event, Category
from .serializers import EventSerializer, CategorySerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('day')
    serializer_class = EventSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
