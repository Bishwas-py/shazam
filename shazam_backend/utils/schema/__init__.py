import graphene

from graphene_django.debug import DjangoDebug
from .schemas import all_queries, all_mutations


class Query(
    *all_queries,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(
    *all_mutations,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation)
