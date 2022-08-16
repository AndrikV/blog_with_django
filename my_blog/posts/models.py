from django.db import models
from django.core.exceptions import ValidationError


class Posts(models.Model):
    title = models.CharField(max_length=256)
    short_description = models.CharField(max_length=512)
    html_content = models.TextField()
    datetime_of_publication = models.DateTimeField(
        'datetime_of_publication', auto_now_add=True
    )


class PostsMedia(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    media_path = models.FileField(upload_to='posts_media')


class PostsAssessments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    assessment = models.IntegerField()

    def clean(self):
        if self.assessment not in [1, 2, 3, 4, 5]:
            raise ValidationError(
                'Invalid assessment (%(assessment)d): value not in range 1-5',
                params={'assessment': self.assessment},
            )


class PostsComments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author = models.CharField(max_length=256, null=True)
    text = models.TextField()
    datetime_of_publication = models.DateTimeField(auto_now_add=True)
