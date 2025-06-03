from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from blog.serializers.comment import CommentCreateSerializer

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]
