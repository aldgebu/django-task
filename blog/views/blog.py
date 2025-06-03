from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from blog.serializers.blog import BlogCreateSerializer


class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer
    permission_classes = [IsAuthenticated]
