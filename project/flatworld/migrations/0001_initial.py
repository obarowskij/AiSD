# Generated by Django 4.2.7 on 2024-04-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Adventure",
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
                ("world", models.ImageField(upload_to="images/")),
                ("hull", models.JSONField()),
                (
                    "fence_build_cost",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
    ]
