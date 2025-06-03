from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from blog.models.blog import Blog
from blog.serializers.blog import BlogCreateSerializer, BlogUpdateSerializer
from blog.permissions import IsBlogAuthor


class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer
    permission_classes = [IsAuthenticated]


class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogUpdateSerializer
    permission_classes = [IsAuthenticated, IsBlogAuthor]


class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated, IsBlogAuthor]
