from django.db import models
from model_utils.managers import InheritanceManager
# Create your models here.

from strawberry_graphql_permission_extension.utils import Role
from strawberry_graphql_permission_extension.utils import BaseOwnerFieldEnum


class OwnerFieldEnum(BaseOwnerFieldEnum):
    USER = 'user'



class UserRoleChoices(models.TextChoices):
    USER = 'user', 'User'
    ADMIN = 'admin', 'Admin'


class IsUser(Role): # Role subclass is redundant, but it is recommended to use it for clarity
    @staticmethod
    def has_permission(info) -> bool:
        user = info.context.user
        return user.role == UserRoleChoices.USER


class UnifiedModel(models.Model):
    objects = InheritanceManager()


class User(UnifiedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    some_field = models.CharField(max_length=100)
    random_model = models.ForeignKey('RandomModel', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=UserRoleChoices.choices, default=UserRoleChoices.USER)

    @property
    def is_anonymous(self):
        return False
    def __str__(self):
        return self.name



class RandomModel(UnifiedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    CREATE_ALLOWED_ROLES = [IsUser]