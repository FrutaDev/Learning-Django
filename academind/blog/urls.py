from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="landing-page"),
    path('posts/', views.posts, name="posts-page"),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), 
         name="detail-post-page"), 
]