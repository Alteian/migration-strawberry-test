import strawberry
from strawberry.schema import Schema

from strawberry_django.optimizer import DjangoOptimizerExtension

from core.user.graphql.queries import Query as UserQuery

schema = Schema(query=UserQuery, extensions=[DjangoOptimizerExtension])
