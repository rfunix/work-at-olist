from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Channel(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "Channel"


class Category(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True,
                            db_index=True, default=None)
    name = models.CharField(max_length=30)
    channel = models.ForeignKey(Channel, related_name='categories')

    class Meta:
        db_table = "Category"

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return '%d: %s' % (self.id, self.name)
