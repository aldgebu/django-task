from django.urls import path
from blog.views.blog import BlogCreateView, BlogUpdateView, BlogDeleteView
from blog.views.comment import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
] 