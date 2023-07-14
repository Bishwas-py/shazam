import graphene
from graphene_django import DjangoObjectType
from general.models import SiteInfo


class SiteInfoNode(DjangoObjectType):
    class Meta:
        model = SiteInfo
        filter_fields = ["id", 'name', 'description', 'author', 'domain', 'url', 'email']
        fields = ("id", 'name', 'description', 'author', 'domain', 'url', 'email')
        interfaces = (graphene.relay.Node,)


class SiteInfoMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        author = graphene.String(required=True)
        description = graphene.String(required=False)
        domain = graphene.String(required=True)
        url = graphene.String(required=True)
        email = graphene.String(required=True)

    site_info = graphene.Field(SiteInfoNode)

    @classmethod
    def mutate(cls, root, info, name, description, author, domain, url, email):
        site_info = SiteInfo.objects.first()
        if not site_info:
            site_info = SiteInfo.objects.create(
                name=name,
                description=description,
                author=author,
                domain=domain,
                url=url,
                email=email,
            )
        else:
            site_info.name = name
            site_info.description = description
            site_info.author = author
            site_info.domain = domain
            site_info.url = url
            site_info.email = email
            site_info.save()
        return SiteInfoMutation(site_info=site_info)


class Query(graphene.ObjectType):
    site_info = graphene.Field(SiteInfoNode)
    site_by_domain = graphene.Field(SiteInfoNode, domain=graphene.String(required=True))

    def resolve_site_by_domain(self, info, domain):
        return SiteInfo.objects.get(domain=domain)

    def resolve_site_info(self, info):
        return SiteInfo.objects.first()


class Mutation(graphene.ObjectType):
    create_site_info = SiteInfoMutation.Field()
