import typing
import strawberry
import strawberry_django
from strawberry.tools import merge_types

from .types import UserType, RandomModelType, SecondUserType

@strawberry.type
class SecondUserQuery:
    #second_user: typing.Optional[SecondUserType] = strawberry_django.field()
    ...



@strawberry.type
class UserQuery: # <-- If named otherwise than Query pk arg is not generated
    user: typing.Optional[UserType] = strawberry_django.node()
    user_connection: strawberry_django.relay.ListConnectionWithTotalCount[UserType] = strawberry_django.connection()
    random_model: typing.Optional[RandomModelType] = strawberry_django.node()
    random_model_connection: strawberry_django.relay.ListConnectionWithTotalCount[RandomModelType] = strawberry_django.connection()
    second_user: SecondUserType = strawberry_django.field()

Query = merge_types(name="Query", types=(UserQuery, SecondUserQuery))
