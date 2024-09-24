from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field


class Graph(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        unique=True
    )
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])
    
    
class spindelData(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    spindle_id = models.CharField(max_length=200)
    token = models.CharField(max_length=200)
    gravity_unit = models.CharField(max_length=200)
    temp_units = models.CharField(max_length=200)
    interval = models.PositiveSmallIntegerField()
    temperature = models.PositiveSmallIntegerField()
    gravity = models.PositiveSmallIntegerField()
    angle = models.IntegerField()
    battery = models.PositiveSmallIntegerField()
    RSSI = models.IntegerField()
    corr_gravity = models.PositiveSmallIntegerField()
    run_time = models.PositiveSmallIntegerField()
    date = models.DateTimeField(("Date"), auto_now_add = True)
