from mongoengine import *

# Create your models here.
class ProductType(Document):
    name = StringField(max_length=100, unique=True, required=True)
    description = StringField(max_length=255)

    class Meta:
        verbose_name = 'product_type'
        verbose_name_plural = 'product_types'
