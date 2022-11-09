from django.db import models

# Create your models here.
class Post(models.Model):
    # user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="user")
    author = models.ForeignKey(
        "User", on_delete=models.CASCADE, null=True, related_name="posts"
    )


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    # post = models.ForeignKey("Post", on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    author = models.ForeignKey(
        "User", related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
