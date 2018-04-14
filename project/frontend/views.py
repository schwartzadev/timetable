from django.http import HttpResponse
from project.timetable.models import Event, Category
from django.template import loader

from datetime import date


def index(request):
    events = Event.objects.order_by('day')
    categories = Category.objects.order_by('name')
    template = loader.get_template('timetable/index.html')
    context = {
        'events': events,
        'categories': categories,
        'today': date.today()
    }
    return HttpResponse(template.render(context, request))


def event(request, event_id):
    temp = 'this event is called {0} and has an id of {1}'
    return HttpResponse(temp.format('temptitle', event_id))


def category(request, category_id):
    info = 'category with id {0}'
    return HttpResponse(info.format(category_id))
