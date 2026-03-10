# courses/models.py
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add the ImageField here as discussed
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    # This field MUST exist for 'filter_horizontal' to work in admin.py
    instructors = models.ManyToManyField('instructors.Instructor', related_name='courses')

    def __str__(self):
        return self.name