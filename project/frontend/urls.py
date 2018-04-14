from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('e/<int:event_id>/', views.event),
    path('c/<int:category_id>/', views.category)
]
