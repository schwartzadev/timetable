from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    # todo add user foreign key and table
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    day = models.DateField()
    is_task = models.BooleanField(default=True, blank=True)
    complete = models.BooleanField(default=False)   # blank if is_task is True
    details = models.CharField(max_length=500, blank=True, default='')
    color = models.CharField(max_length=6)  # not blank -- auto assign color if not provided
    time = models.TimeField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title
