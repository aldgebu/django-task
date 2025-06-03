from django.urls import path
from blog.views.blog import BlogCreateView
from blog.views.comment import CommentCreateView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
] 