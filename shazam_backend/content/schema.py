# cookbook/schema.py
import graphene
from django.utils.text import slugify
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth.models import User

from content.models import Category, Post, Tag

import django_filters


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ["id", "name", "slug", "created_at", "updated_at"]
        fields = ("id", "name", "slug", "created_at", "updated_at")
        interfaces = (graphene.relay.Node,)


class TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = ["id", "name", "slug", "created_at", "updated_at"]
        fields = ("id", "name", "slug", "created_at", "updated_at")
        interfaces = (graphene.relay.Node,)


class PostNode(DjangoObjectType):
    tags = DjangoFilterConnectionField(TagNode)
    username = graphene.String()
    true_slug = graphene.String()

    def resolve_true_slug(self, info):
        return self.user.username + "/" + self.slug

    def resolve_username(self, info):
        return self.user.username

    class Meta:
        model = Post
        fields = (
            "id", "user", "title",
            "body", "category", "slug",
            "tags", "keywords",
            "created_at", "updated_at",
        )
        filter_fields = {
            'slug': ['exact'],
            'id': ['exact'],
            'user': ['exact'],
            'title': ['exact', 'icontains', 'istartswith'],
            'body': ['exact', 'icontains'],
            'category': ['exact'],
            'tags': ['exact'],
            'keywords': ['exact', 'icontains'],
            'created_at': ['exact', 'icontains', 'istartswith'],
            'updated_at': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node,)


class PostMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        category = graphene.String(required=True)
        tags = graphene.List(graphene.String, required=False)  # check if tags are valid; max 5 tags allowed
        keywords = graphene.String(required=False)
        slug = graphene.String(required=False)

    post = graphene.Field(PostNode)

    @classmethod
    def mutate(cls, root, info, title, body, category, tags, keywords, slug):
        category_slug = slugify(category)

        # Check if a category with the same slug already exists
        category_instance = Category.objects.filter(slug=category_slug).first()

        if not category_instance:
            category_instance = Category.objects.create(name=category, slug=category_slug, added_by=info.context.user)

        post = Post.objects.create(
            user=info.context.user,
            title=title,
            body=body,
            category=category_instance,
            keywords=keywords,
            slug=slugify(slug),
        )

        for tag in tags:
            tag_slug = slugify(tag)
            tag_instance = Tag.objects.filter(slug=tag_slug).first()

            if not tag_instance:
                tag_instance = Tag.objects.create(name=tag, slug=tag_slug, added_by=info.context.user)

            post.tags.add(tag_instance)

        post.save()

        return PostMutation(post=post)  # noqa: F821


class Query(graphene.ObjectType):
    all_posts = DjangoFilterConnectionField(PostNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
    all_tags = DjangoFilterConnectionField(TagNode)

    post = graphene.relay.Node.Field(PostNode)
    category = graphene.relay.Node.Field(CategoryNode)
    post_by_slug = graphene.Field(PostNode, slug=graphene.String(required=True),
                                  username=graphene.String(required=True))

    def resolve_post_by_slug(self, info, slug, username):
        user = User.objects.get(username=username)
        return Post.objects.get(slug=slug, user=user)


class Mutation(graphene.ObjectType):
    create_post = PostMutation.Field()
