from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    some_field = models.CharField(max_length=100)
    random_model = models.ForeignKey('RandomModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class RandomModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
