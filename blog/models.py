from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    posted_data = models.DateTimeField(auto_now_add=True)
    # auto_now_add=Trueで現在の時刻を自動で入力してくれる


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_data = models.DateTimeField(auto_now=True)
