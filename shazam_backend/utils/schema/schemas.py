from general import schema as general_schema
from content import schema as content_schema

all_queries = [
    general_schema.Query,
    content_schema.Query,
]

all_mutations = [
    general_schema.Mutation,
    content_schema.Mutation,
]
