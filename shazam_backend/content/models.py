from typing import Optional

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    keywords = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(fields=['slug', 'user'], name='unique_slug')
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.create_slug()
        super(Post, self).save(*args, **kwargs)

    def create_slug(self):
        if not self.slug:
            self.slug = slugify(self.title)
            posts_with_same_slugs = Post.objects.filter(slug=self.slug, user=self.user)
            if posts_with_same_slugs.exists():
                self.slug = f"{self.slug}-{timezone.now().timestamp()}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Category(models.Model):
    added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def create_slug(self):
        if not self.slug:
            self.slug = slugify(self.name)

    def save(self, *args, **kwargs):
        self.create_slug()
        super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    added_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def create_slug(self):
        if not self.slug:
            self.slug = slugify(self.name)

    def save(self, *args, **kwargs):
        self.create_slug()
        super(Tag, self).save(*args, **kwargs)
