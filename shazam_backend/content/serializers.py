
from rest_framework import serializers
from content.models import Post, Category, Tag
from helpers.sanitizer import sanitize_content

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
    
    def is_valid(self, raise_exception=False):
        if self.initial_data['body']:
            self.initial_data['body'] = sanitize_content(self.initial_data['body'])
        
        if self.initial_data['excerpt']:
            self.initial_data['excerpt'] = sanitize_content(self.initial_data['excerpt'])

        return super().is_valid(raise_exception=raise_exception)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
