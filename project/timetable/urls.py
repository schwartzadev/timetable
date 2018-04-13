from rest_framework import routers
from project.timetable.views import EventsViewSet, CategoriesViewSet

router = routers.DefaultRouter()
router.register(r'events', EventsViewSet)
router.register(r'categories', CategoriesViewSet)

urlpatterns = router.urls
