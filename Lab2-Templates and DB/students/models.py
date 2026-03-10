# students/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name