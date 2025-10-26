from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect

from .models import Post, Subscriber, Comment
from .forms import SubscriberForm, CommentForm

class IndexView(View):
    def get(self, request):
        form = SubscriberForm()
        latest_posts = Post.objects.all().order_by("-date")[:3]
        return render(request, "blog/home.html", {
            "posts": latest_posts,
            "form": form
        })
    
    def post(self, request):
        form = SubscriberForm(request.POST)
        exists_email = Subscriber.objects.filter(email=request.POST['email']).first()
        
        if form.is_valid():
            if exists_email is not None:
                form.add_error("email", "Este correo ya está suscrito.")
            else:
                form.save()
                return HttpResponseRedirect("/")
        latest_posts = Post.objects.all().order_by("-date")[:3]
        return render(request, "blog/home.html", {
            "form": form,
            "posts": latest_posts
            })




def get_date(post):
    return post.date

def posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/home.html", {
        "posts": posts               
    })

# def all_posts(request):
#     posts = Post.objects.all()
#     return render(request, "blog/all-posts.html", {
#         "posts": posts
#     })

class PostDetailView(View):
    def get(self, request, slug):
        form = CommentForm()
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
            "tags": detailed_post.tags.all(),
            "form": form,
            "comments": detailed_post.comments.filter(is_approved=True),
            "slug": slug

    })

    def post(self, request, slug):
        form = CommentForm(request.POST)
        detailed_post = get_object_or_404(
            Post,
            slug=slug
        )
        comments_post = Comment.objects.filter(post=detailed_post, is_approved=True)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = detailed_post
            comment.save()
            return HttpResponseRedirect(f"/posts/{slug}")
        return render(request, "blog/post.html", {
            "title": detailed_post.title,
            "content": detailed_post.content,
            "date": detailed_post.date,
            "image": detailed_post.image,
            "author": detailed_post.author,
            "tags": detailed_post.tags.all(),
            "form": form,
            "comments": comments_post
        })