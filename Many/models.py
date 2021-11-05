from django.db import models


# Create your models here.
class Sauce(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Sandwich(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200, null=True)
    sauces = models.ManyToManyField(Sauce, related_name="sandwiches")

    def __str__(self):
        return self.name