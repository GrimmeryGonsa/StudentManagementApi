from django.db import models


# Create your models here.

class Institute(models.Model):
    TYPE = (
        ("h", "High School"),
        ("C", "College"),
    )
    name = models.CharField(max_length=200)
    type_of_institute = models.CharField(max_length=1, choices=TYPE)

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDERS = (
        ("f", "Female"),
        ("m", "Male"),
        ("u", "Undisclosed"),
    )
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.CharField(max_length=150)
    gender = models.CharField(max_length=1, choices=GENDERS)
    percentage = models.FloatField()
    Institute = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
