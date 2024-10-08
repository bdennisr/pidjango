from django.db import models
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field


class Recipe(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        unique=True
    )
    description = models.TextField()
    content = models.TextField() 
    author = models.CharField(
        max_length=200
    )
    date = models.DateTimeField(("Date"), auto_now_add = True)
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('recipe_detail',  kwargs={"pk": self.pk})
    
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]
