from rest_framework import serializers
from blog.models.blog import Blog


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'picture_url', 'description']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context['request'].user
        return Blog.objects.create(author=user, **validated_data)


class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'picture_url', 'description']
        read_only_fields = ['id']
