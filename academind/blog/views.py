from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post

# fake_posts = [
#     {
#         "title": "My first post",
#         "content": "This is my first post",
#         "slug": "my-first-post",
#         "image": "blog/images/django.png",
#         "date": date(2024,6,2),
#         "author": "Ronaldo",
#         "image": ""
#     },
#     {
#         "title": "My second post",
#         "content": "This is my second post",
#         "slug": "my-second-post",
#         "image": "blog/images/django.png",
#         "date": date(2024,6,2),
#         "author": "Ronaldo",
#         "image": ""
#     },
# ]

def get_date(post):
    return post.date

def posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/home.html", {
        "posts": posts               
    })

def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/home.html", {
        "posts": latest_posts,
    })

# def all_posts(request):
#     posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", {
#         "posts": posts
#     })

def one_post(request, slug):
    detailed_post = get_object_or_404(
        Post,
        slug=slug
    )
    return render(request, "blog/post.html", {
        "title": detailed_post.title,
        "content": detailed_post.content,
        "date": detailed_post.date,
        "image": detailed_post.image,
        "author": detailed_post.author,
        "tags": detailed_post.tags.all()
    })