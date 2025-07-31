from django.db import models

# Create your models here.


class Book(models.Model):
    # what we want to add
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher=models.CharField(max_length=200)
    edition=models.SmallIntegerField()
    pages=models.IntegerField()
    price=models.DecimalField(max_digits=5, decimal_places=2)

    # to display name in db 
    def __str__(self):
        return self.title
    
