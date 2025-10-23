from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
    
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default="",blank=True, null=False, max_length=100, db_index=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="blog/images", null=True, blank=True)
    author = models.ForeignKey("Author", related_name="posts", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)

    def get_absolute_url(self):
        return reverse("model_detail", args=[self.slug])
    
    def save (self, *args, **kwargs):
        self.slug = slugify(self.title) 
        super().save(*args, **kwargs)



class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    