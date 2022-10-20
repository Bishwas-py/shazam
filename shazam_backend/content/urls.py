# urls for content app

from django.urls import path
from content import views

urlpatterns = [
    path('posts/', views.Posts.as_view(), name='posts'),
    path('categories/', views.Categories.as_view(), name='categories'),
    path('tags/', views.Tags.as_view(), name='tags'),

    path('category/<int:pk>', views.get_category, name='category'),
    path('post/<int:pk>', views.get_post, name='post'),
    path('tag/<int:pk>', views.get_tag, name='tag'),
]
