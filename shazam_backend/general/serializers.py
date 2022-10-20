from rest_framework import serializers
from general.models import SiteInfo


class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = ('name', 'description', 'author', 'domain', 'url', 'email')
