from django.db import models

from general import default


class SiteInfo(models.Model):
    name = models.CharField(max_length=100, default=default.name)
    description = models.TextField(default=default.description)
    author = models.CharField(max_length=100, default=default.author)
    domain = models.CharField(max_length=100, default=default.domain)
    url = models.CharField(max_length=100, default=default.url)
    email = models.CharField(max_length=100, default=default.email)

    def __str__(self):
        return self.name
