from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    keywords = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def create_slug(self):
        slug = slugify(self.name)
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.create_slug()
        super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def create_slug(self):
        slug = slugify(self.name)
        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.create_slug()
        super(Tag, self).save(*args, **kwargs)
