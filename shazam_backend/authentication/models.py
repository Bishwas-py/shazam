import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string

from django.utils import timezone

TOKEN_EXPIRES_MINUTES = 5


class Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)

    token_key = models.CharField(max_length=100, blank=True, null=True)
    token_key_expires = models.DateTimeField(blank=True, null=True)
    last_sent_time = models.DateTimeField(blank=True, null=True)

    def set_token(self):
        token = get_random_string(length=7)
        self.token_key = token
        self.token_key_expires = timezone.now() + timezone.timedelta(minutes=TOKEN_EXPIRES_MINUTES)
        self.save()

    def set_confirmed(self, token_string):
        try:
            self.is_confirmed = True
            self.token_key = None
            self.token_key_expires = None
            self.save()
            return True, "Email confirmed"
        except:
            return False, "Email not confirmed, due to an error"

    def set_confirm_sent(self):
        try:
            self.last_sent_time = timezone.now()
            self.save()
            return True, "Email confirmation sent"
        except:
            return False, "Email confirmation not sent, due to an error"

    def __str__(self):
        return f"{self.user.username} - {self.is_confirmed}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.user.email}"


def create_profile_with_status(sender, **kwargs):
    if kwargs['created']:
        print("Created")
        user_profile = Profile.objects.create(user=kwargs['instance'])
        user_status = Status.objects.create(user=kwargs['instance'])

        user_profile.save()
        user_status.save()


post_save.connect(create_profile_with_status, sender=User)
