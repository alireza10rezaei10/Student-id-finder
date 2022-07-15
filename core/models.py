from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.CharField(max_length=20)
    name           = models.CharField(max_length=200)

    class Meta:
        ordering = ['student_number']

    def __str__(self):
        return self.name