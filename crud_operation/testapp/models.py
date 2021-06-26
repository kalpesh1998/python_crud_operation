from django.db import models

# Create your models here.
class Student_form(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    title = models.CharField(max_length=15)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name