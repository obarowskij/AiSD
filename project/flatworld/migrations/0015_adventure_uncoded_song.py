# Generated by Django 4.2.7 on 2024-05-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flatworld", "0014_adventure_song_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="adventure",
            name="uncoded_song",
            field=models.CharField(max_length=100, null=True),
        ),
    ]