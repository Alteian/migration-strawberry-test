from django.db import models
from model_utils.managers import InheritanceManager
# Create your models here.

class UnifiedModel(models.Model):
    objects = InheritanceManager()


class User(UnifiedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    some_field = models.CharField(max_length=100)
    random_model = models.ForeignKey('RandomModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class RandomModel(UnifiedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
