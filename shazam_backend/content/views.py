# views for the content app, with the serializers imported
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from content.serializers import PostSerializer, CategorySerializer, TagSerializer
from content.models import Post, Category, Tag


class Posts(APIView):
    def get(self, request):
        posts = Post.objects.all()
        posts = PostSerializer(posts, many=True)
        return Response(posts.data, status=status.HTTP_200_OK)

    @permission_classes([IsAuthenticated])
    def post(self, request):
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def put(self, request):
        post = get_object_or_404(Post, pk=request.data['id'])
        post = PostSerializer(post, data=request.data, partial=True)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_202_ACCEPTED)
        return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request):
        post = get_object_or_404(Post, pk=request.data['id'])
        post.delete()
        return Response("Post deleted", status=status.HTTP_204_NO_CONTENT)


class Categories(APIView):
    def get(self, request, **kwargs):
        categories = Category.objects.all()
        categories = CategorySerializer(categories, many=True)
        return Response(categories.data, status=status.HTTP_200_OK)

    @permission_classes([IsAuthenticated])
    def post(self, request):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_201_CREATED)
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def put(self, request):
        category = get_object_or_404(Category, pk=request.data['id'])
        category = CategorySerializer(category, data=request.data, partial=True)
        if category.is_valid():
            category.save()
            return Response(category.data, status=status.HTTP_202_ACCEPTED)
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request):
        category = get_object_or_404(Category, pk=request.data['id'])
        category.delete()
        return Response("Category deleted", status=status.HTTP_204_NO_CONTENT)


class Tags(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        tags = TagSerializer(tags, many=True)
        return Response(tags.data, status=status.HTTP_200_OK)

    @permission_classes([IsAuthenticated])
    def post(self, request):
        tag = TagSerializer(data=request.data)
        if tag.is_valid():
            tag.save()
            return Response(tag.data, status=status.HTTP_201_CREATED)
        return Response(tag.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def put(self, request):
        tag = get_object_or_404(Tag, pk=request.data['id'])
        tag = TagSerializer(tag, data=request.data, partial=True)
        if tag.is_valid():
            tag.save()
            return Response(tag.data, status=status.HTTP_202_ACCEPTED)
        return Response(tag.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request):
        tag = get_object_or_404(Tag, pk=request.data['id'])
        tag.delete()
        return Response("Tag deleted", status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
# set permission to authenticated only
def get_category(request, pk):
    print(request.headers['Authorization'])
    category = get_object_or_404(Category, pk=pk)
    category = CategorySerializer(category)
    return Response(category.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post = PostSerializer(post)
    return Response(post.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag = TagSerializer(tag)
    return Response(tag.data, status=status.HTTP_200_OK)
