from django.db import models
from django.contrib.auth import get_user_model

from general import defaults


class SiteSocial(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site Social"
        verbose_name_plural = "Site Socials"


class SiteReview(models.Model):
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField(default=0)
    review = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rater} rated {self.rate}"

    class Meta:
        verbose_name = "Site Rate"
        verbose_name_plural = "Site Rates"


class Feedback(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"


class SiteInfo(models.Model):
    name = models.CharField(max_length=100, default=defaults.name)
    description = models.TextField(default=defaults.description)
    author = models.CharField(max_length=100, default=defaults.author)
    domain = models.CharField(max_length=100, default=defaults.domain)
    url = models.CharField(max_length=100, default=defaults.url)
    email = models.EmailField(default=defaults.email)
    logo = models.ImageField(upload_to="site_info", blank=True)
    socials = models.ManyToManyField(SiteSocial, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site Information"
        verbose_name_plural = "Site Information"
