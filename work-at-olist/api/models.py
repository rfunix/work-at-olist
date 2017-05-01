from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Channel(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = "Channel"

    def __str__(self):
        return self.name

class Category(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True,
                            db_index=True, default=None,
                            related_name='children')
    name = models.CharField(max_length=30)
    channel = models.ForeignKey(Channel, related_name='categories')

    def __str__(self):
        return ("%s:%s:%s" % (self.channel.name, self.name, self.parent.name))

    class Meta:
        db_table = "Category"

    class MPTTMeta:
        order_insertion_by = ['name']
