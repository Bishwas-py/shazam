# tests for content app

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from content.models import Post, Category, Tag


class PostTests(APITestCase):
    def test_create_post(self):
        """
        Ensure we can create a new post object.
        """
        url = reverse('posts')
        tag = Tag.objects.create(name='#test')
        category = Category.objects.create(name='test')
        data = {
            'title': 'Test Post', 'category': category.id,
            'tags': [tag.id], 'keywords': 'test, test2',
            'body': 'test'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_update_post(self):
        """
        Ensure we can update a post object.
        """
        tag = Tag.objects.create(name='#test')
        category = Category.objects.create(name='test')
        post = Post.objects.create(
            title='Test Post', category=category, keywords='test, test2', body='test'
        )
        post.tags.add(tag)
        url = reverse('posts')
        data = {
            'id': post.id, 'title': 'Test Post Updated',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post Updated')

    def test_delete_post(self):
        """
        Ensure we can delete a post object.
        """
        tag = Tag.objects.create(name="#test")
        category = Category.objects.create(name='test')
        post = Post.objects.create(
            title='Test Post', keywords='test, test2', body='test',
            category=category
        )
        post.tags.add(tag)
        url = reverse('posts')
        data = {'id': post.id}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)


class CategoryTests(APITestCase):
    def test_create_category(self):
        """
        Ensure we can create a new category
        """
        url = reverse('categories')
        data = {
            'name': 'Test Category'
        }
        response = self.client.post(url, data, follow='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Test Category')

    def test_update_post