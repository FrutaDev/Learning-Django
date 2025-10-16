from django.shortcuts import render
from datetime import date

fake_posts = [
    {
        "title": "My first post",
        "content": "This is my first post",
        "slug": "my-first-post",
        "image": "blog/images/django.png",
        "date": date(2024,6,2),
        "author": "Ronaldo"
    },
    {
        "title": "My second post",
        "content": "This is my second post",
        "slug": "my-second-post",
        "image": "blog/images/django.png",
        "date": date(2024,6,2),
        "author": "Ronaldo"
    },
]

def get_date(post):
    return post['date']

def index(request):
    return render(request, "blog/home.html", {
        "posts": fake_posts
    })

def posts(request):
    sorted_posts = sorted(fake_posts,key=get_date)
    latest_post = sorted_posts[-3:]
    return render(request, "blog/posts.html", {
        "posts": latest_post
    })

def all_posts(request):
    return render(request, "blog/all-posts.html", {
        "posts": fake_posts
    })

def one_post(request, slug):
    detailed_post = next(post for post in fake_posts if post['slug'] == slug)
    return render(request, "blog/post.html", {
        "post": detailed_post
    })