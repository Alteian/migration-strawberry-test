import typing
import strawberry

import strawberry_django

from core.user.models import User, RandomModel

@strawberry_django.type(RandomModel)
class RandomModelType(strawberry.relay.Node):
    id: strawberry.relay.NodeID[int]
    name: strawberry.auto


@strawberry_django.type(User)
class UserType(strawberry.relay.Node):
    id: strawberry.relay.NodeID[int]
    name: strawberry.auto
    email: strawberry.auto
    some_field: strawberry.auto
    random_model: typing.Optional[RandomModelType]
