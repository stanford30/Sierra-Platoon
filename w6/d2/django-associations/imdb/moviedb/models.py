from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    rating = models.CharField(max_length=5)
    runtime = models.TimeField(null=True)
    actors = models.ManyToManyField(Actor, through="Role", related_name="movies")
    # actor = models.ForeignKey(
    #     "Actor", on_delete=models.CASCADE, related_name="movies", null=True
    # )
    # actors = models.ManyToManyField("Actor", through="Role")
    # role = models.ForeignKey(
    #     "Role", on_delete=models.CASCADE, related_name="movies", null=True
    # )
    # roles = models.ManyToManyField('Role', through='Role')
    # class Meta:
    #     unique_together = ("actor", "role")


class Role(models.Model):
    actor = models.ForeignKey(
        "Actor", on_delete=models.CASCADE, related_name="roles", null=True
    )
    movie = models.ForeignKey(
        "Movie", on_delete=models.CASCADE, related_name="roles", null=True
    )

    character_name = models.CharField(max_length=64, null=True)
    number_of_lines = models.IntegerField(null=True)
