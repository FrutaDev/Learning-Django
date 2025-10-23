from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="landing-page"),
    path('posts/', views.posts, name="posts-page"),
    path('posts/<slug:slug>', views.one_post, 
         name="detail-post-page"), 
]