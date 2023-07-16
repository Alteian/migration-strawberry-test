import strawberry
from strawberry.schema import Schema

from strawberry_django.optimizer import DjangoOptimizerExtension

from core.user.graphql.queries import Query as UserQuery
from core.user.graphql.mutations import Mutation as UserMutation

schema = Schema(query=UserQuery, mutation=UserMutation, extensions=[DjangoOptimizerExtension])
