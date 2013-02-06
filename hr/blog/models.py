from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=128,
                           help_text="the title of this blog post")
    body=models.TextField(help_text="the body of the post")
    tags=models.CharField(max_length=128,
                          help_text="Any tags for this post")
