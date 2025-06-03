from rest_framework import serializers
from blog.models.comment import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'blog', 'parent']
        
    def create(self, validated_data):
        user = self.context['request'].user
        return Comment.objects.create(author=user, **validated_data)


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
