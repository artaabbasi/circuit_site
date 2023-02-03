from django.db import models

class Tag(models.Model):
    name = models.TextField()
    text = models.TextField()
    ref_link = models.TextField()


class Item(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.FileField(null=True, blank=True)
