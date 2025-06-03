from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from blog.models.comment import Comment
from blog.serializers.comment import CommentCreateSerializer, CommentUpdateSerializer
from blog.permissions import IsCommentAuthor


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticated, IsCommentAuthor]


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsCommentAuthor]
