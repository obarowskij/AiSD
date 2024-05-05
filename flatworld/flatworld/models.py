from django.db import models


class Adventure(models.Model):
    world = models.ImageField(upload_to="images/", default="")
    hull_points = models.JSONField(null=True, blank=True)
    # world_points = models.JSONField(null=True, blank=True)
    world_points = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )

    inhabitants = models.JSONField(null=True, blank=True)
    bearers = models.IntegerField(null=True)
    factory = models.JSONField(null=True, blank=True)

    fence = models.ImageField(upload_to="images/", default="")
    fence_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )

    song = models.CharField(max_length=100, null=True)
    changed_song = models.CharField(max_length=100, null=True)

    code = models.JSONField(null=True, blank=True)
    coded_song = models.CharField(max_length=100, null=True)

    guards = models.JSONField(null=True, blank=True)
    schedule = models.JSONField(null=True, blank=True)
