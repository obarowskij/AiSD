# Generated by Django 4.2.7 on 2024-05-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flatworld", "0011_alter_adventure_world_points"),
    ]

    operations = [
        migrations.AddField(
            model_name="adventure",
            name="fence_neighbors",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
