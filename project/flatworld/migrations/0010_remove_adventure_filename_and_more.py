# Generated by Django 4.2.7 on 2024-05-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flatworld", "0009_adventure_filename"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="adventure",
            name="filename",
        ),
        migrations.AlterField(
            model_name="adventure",
            name="world_points",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
