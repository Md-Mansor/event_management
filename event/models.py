from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name
    
class Event(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")

    def __str__(self):
        return self.name

class Participant(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    event=models.ManyToManyField(Event)
    
    def __str__(self):
        return self.name