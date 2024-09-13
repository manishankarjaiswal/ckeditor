from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # This field will use CKEditor with upload capabilities

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Simple TextField for the content
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

