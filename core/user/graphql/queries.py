import typing
import strawberry
import strawberry_django

from .types import UserType, RandomModelType

@strawberry.type
class Query:
    user: typing.Optional[UserType] = strawberry_django.node()
    user_connection: strawberry_django.relay.ListConnectionWithTotalCount[UserType] = strawberry_django.connection()
    random_model: typing.Optional[RandomModelType] = strawberry_django.node()
    random_model_connection: strawberry_django.relay.ListConnectionWithTotalCount[RandomModelType] = strawberry_django.connection()
