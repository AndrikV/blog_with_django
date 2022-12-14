# Generated by Django 4.1 on 2022-08-21 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Posts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256)),
                ("short_description", models.CharField(max_length=512)),
                ("html_content", models.TextField()),
                (
                    "datetime_of_publication",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="datetime_of_publication"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PostsMedia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("media_name", models.CharField(max_length=256)),
                ("media_file", models.FileField(upload_to="posts_media")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.posts"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PostsComments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.CharField(max_length=256, null=True)),
                ("text", models.TextField()),
                ("datetime_of_publication", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.posts"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PostsAssessments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("assessment", models.IntegerField()),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.posts"
                    ),
                ),
            ],
        ),
    ]
