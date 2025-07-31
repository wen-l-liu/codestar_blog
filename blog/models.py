from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    # This is the author of the blog article.
    # The cascade on delete means that on the deletion of the user entry
    # all their posts are also deleted.
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    # This is the blog article content.
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        # This means that the most recent posts are shown first.

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`blog.Post`
    and :model:`auth.User`.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    # This is the blog article that the comment is associated with.
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commentor"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
        # This means that the most recent comments are shown first.

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
