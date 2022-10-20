# urls for content app

from django.urls import path
from content import views

urlpatterns = [
    path('posts/', views.Posts.as_view(), name='posts'),
    path('categories/', views.Categories.as_view(), name='categories'),
    path('tags/', views.Tags.as_view(), name='tags'),
]
