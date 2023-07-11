import typing
import strawberry

import strawberry_django
from strawberry_django import field

from core.user.models import User, RandomModel
from strawberry_django.filters import FilterLookup
@strawberry_django.filter(User, lookups=True)
class UserFilter:
    id: typing.Optional[FilterLookup[strawberry.relay.GlobalID]]
    name: strawberry.auto
    some_field: strawberry.auto


@strawberry_django.type(RandomModel)
class RandomModelType(strawberry.relay.Node):
    id: strawberry.relay.NodeID[int]
    name: strawberry.auto


@strawberry_django.type(User, filters=UserFilter)
class UserType(strawberry.relay.Node):
    #code: strawberry.relay.NodeID[int] = field(graphql_type=strawberry.relay.GlobalID, field_name="id")
    name: strawberry.auto
    super_email: strawberry.auto = field(field_name="email")
    some_field: strawberry.auto
    #random_model: typing.Optional[int] = field(field_name="random_model_pk")
    random_model_id: typing.Optional[int]
    random_model: typing.Optional[int] = field(field_name="random_model_id")