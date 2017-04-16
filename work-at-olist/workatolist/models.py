from django.db import models


class Channel(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "Channel"


class Category(models.Model):
    parent = models.ForeignKey("self", null=True)
    name = models.CharField(max_length=30)
    channel = models.ForeignKey(Channel)

    class Meta:
        db_table = "Category"
