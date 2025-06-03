from rest_framework import serializers
from blog.models.blog import Blog


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'picture_url', 'description']

    def create(self, validated_data):
        user = self.context['request'].user

        return Blog.objects.create(author=user, **validated_data)
