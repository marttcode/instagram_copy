"""Posts URLS"""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),

    path(
        route='posts/new/', 
        view=views.new_post, 
        name='new_post'
    ),

    path(
        route='posts/<int:post_id>', 
        view=views.PostDetailView.as_view(), 
        name='post_detail'
    ),

]
