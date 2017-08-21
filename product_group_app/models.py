from mongoengine import *

# Create your models here.
class ProductGroup(Document):
    name = StringField(max_length=100, unique=True, required=True)
    description = StringField(max_length=255, null=True)
    product_type = ReferenceField('ProductType', required=True)

    class Meta:
        verbose_name = 'product_group'
        verbose_name_plural = 'product_groups'
