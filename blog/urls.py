from django.urls import path
from . import views
from .views import (
	PostListView,
	PostCreateView,
	PostDetailView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView

	)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name="blog-about"),
    
    #so we would expect for this to have post_create template, but it shares the template 
    #with post update view and thus has a template post_form

    
]

