from django.urls import path, include
from . import views

urlpatterns = [
    path('create_post/', views.PostView.as_view(), name='create_post'),
    path('list_post/', views.ListPostView.as_view(), name='list_post'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('comment/', views.CommentView.as_view(), name='comment'),
]