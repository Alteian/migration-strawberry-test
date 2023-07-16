import typing
import strawberry
import strawberry_django

from django.db import IntegrityError, models
from django.contrib.auth import get_user_model
from strawberry.relay import GlobalID
from strawberry.types import Info
from strawberry_graphql_permission_extension.extensions import HasPermissionToCreate, HasPermissionToInteract
from strawberry_graphql_permission_extension.utils import PermissionCaseSwitcher

from core.user.models import RandomModel, OwnerFieldEnum, User
from .inputs import CreateRandomModelInput
from .payloads import (
    CreateRandomModelPayload,
    CreateRandomModelError,
    CreateRandomModelSuccess
    )


def resolve_case_user(info, instance) -> bool:
    if isinstance(instance, User):
        user = instance
    else:
        if field := getattr(instance, "OWNER_FIELD", False):
            user = getattr(instance, field)
    if user and user == info.context.user:
        return True
    return False


class CustomPermissionCaseSwitcher(PermissionCaseSwitcher):

    def case_user(self) -> bool:
        return resolve_case_user(self.info, self.instance)
    
    @classmethod
    def resolve_case(cls, info, instance):
        if isinstance(instance, User):
            return cls(info, instance, case="user").switch()
class CustomHasPermissionToInteract(HasPermissionToInteract):
    permission_case_switcher = CustomPermissionCaseSwitcher     


@strawberry.type
class Mutation:
    @strawberry.mutation(extensions=[HasPermissionToCreate(RandomModel)])
    def create_random_model(self, info: Info, input: CreateRandomModelInput) -> CreateRandomModelPayload:
        try:
            random_model = RandomModel.objects.create(**input.__dict__)
            return CreateRandomModelSuccess(random_model=random_model)
        except IntegrityError:
            return CreateRandomModelError()

    @strawberry.mutation(extensions=[CustomHasPermissionToInteract()])
    def update_user(self, info: Info, id: GlobalID, name: str) -> bool:
        user = id.resolve_node_sync(info)
        user.name = name
        user.save()
        return True
        