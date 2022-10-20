# tests for content app

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from content.models import Post, Category, Tag


class PostTests(APITestCase):
    def test_create_post(self):
        """
        Ensure we can create a new post object; use all required field to create post
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
        Ensure we can update a post object;
        use id, title [or any] field to check post update
        """
        tag = Tag.objects.create(name='#test')
        category = Category.objects.create(name='test')
        post = Post.objects.create(
            title='Test Post', category=category, keywords='test, test2', body='test'
        )
        post.tags.add(tag)
        url = reverse('posts')
        new_title = 'Test Post Updated'

        data = {
            'id': post.id, 'title': new_title,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, new_title)

    def test_delete_post(self):
        """
        Ensure we can delete a post object;
        use `id` to check delete post
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
        Ensure we can create a new category;
        use `name` [or with `slug`] to create category
        """
        url = reverse('categories')
        data = {
            'name': 'Test Category'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Test Category')

    def test_update_category(self):
        """
        Ensure we can update the category;
        use `slug` [or `name`] to check updates
        """
        url = reverse('categories')
        category = Category.objects.create(
            name='Test Category'
        )
        new_slug = 'test-category-updated'
        data = {
            'id': category.id,
            'slug': new_slug
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Category.objects.get().slug, new_slug)

    def test_delete_category(self):
        category = Category.objects.create(
            name='Test Category'
        )
        url = reverse('categories')
        data = {
            'id': category.id
        }
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)


class TagTests(APITestCase):
    def test_create_tag(self):
        """
        Ensure we can create a new tag;
        use `name` to create tag
        """
        url = reverse('tags')
        data = {
            'name': '#test'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 1)
        self.assertEqual(Tag.objects.get().name, '#test')

    def test_update_tag_(self):
        """
        Ensure we can update the tag;
        use id and `slug` [or name] to check updates
        """
        url = reverse('tags')
        tag = Tag.objects.create(
            name='#test'
        )
        new_slug = 'test-updated'
        data = {
            'id': tag.id,
            'slug': new_slug
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(Tag.objects.get().slug, new_slug)

    def test_delete_tag(self):
        tag = Tag.objects.create(
            name='#test'
        )
        url = reverse('tags')
        data = {
            'id': tag.id
        }
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)
