from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):
    Title = models.CharField(max_length=200, blank = True, null = True)
    Director = models.CharField(max_length=100, blank = True, null = True)
    Year = models.IntegerField(blank = True, null = True)
    Rating = models.DecimalField( blank = True, null = True,max_digits=10,decimal_places=4)
    poster = models.CharField( max_length=50, blank = True, null = True)
    slug = models.SlugField(default = 'test')

    def __str__(self):
        return self.name
