from django.db import models


class Polls(models.Model):
    question = models.CharField(max_length=256)
    description = models.TextField(null=True)
    allow_multi_choices = models.BooleanField(default=False)
    datetime_of_publication = models.DateTimeField(auto_now_add=True)
    number_of_votes = models.IntegerField(default=0)


class Choices(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    number_of_times_selected = models.IntegerField(default=0)