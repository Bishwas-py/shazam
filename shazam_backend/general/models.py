from django.db import models
from django.contrib.auth import get_user_model

import requests
from bs4 import BeautifulSoup
from general import default


class SiteSocial(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, default=default.icon)

    def __str__(self):
        return self.name

    def fetch_save_icon(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            icon = soup.find('link', rel='shortcut icon')
            if icon:
                self.icon = icon['href']
                self.save()

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
    name = models.CharField(max_length=100, default=default.name)
    description = models.TextField(default=default.description)
    author = models.CharField(max_length=100, default=default.author)
    domain = models.CharField(max_length=100, default=default.domain)
    url = models.CharField(max_length=100, default=default.url)
    email = models.CharField(max_length=100, default=default.email)
    socials = models.ManyToManyField(SiteSocial, blank=True)
    site_reviews = models.ManyToManyField(SiteReview, blank=True)
    feedbacks = models.ManyToManyField(Feedback, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site Information"
        verbose_name_plural = "Site Information"
