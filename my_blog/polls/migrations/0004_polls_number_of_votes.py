# Generated by Django 4.1 on 2022-08-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_choices_number_of_times_selected"),
    ]

    operations = [
        migrations.AddField(
            model_name="polls",
            name="number_of_votes",
            field=models.IntegerField(default=0),
        ),
    ]
