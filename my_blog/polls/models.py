from django.db import models


class Polls(models.Model):
    question = models.CharField(max_length=256)
    description = models.TextField(null=True)
    allow_multi_choices = models.BooleanField(default=False)
    datetime_of_publication = models.DateTimeField(auto_now_add=True)


class Choices(models.Model):
    poll = models.ForeignKey(Polls)
    name = models.CharField(max_length=256)
    author_info = models.CharField(max_length=256, null=True)
    