from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('create', views.create, name='create'),
    path('/<int:pk>', views.PostsDetail.as_view(), name='posts-detail'),
    path('/<int:pk>/update', views.PostsUpdate.as_view(), name='posts-update'),
    path('/<int:pk>/delete', views.PostsDelete.as_view(), name='posts-delete')
]