from mongoengine import *

# Create your models here.
class ProductDetail(EmbeddedDocument):
    brand = StringField(verbose_name="Brand", null=True)
    series = StringField(verbose_name="Series", null=True)
    code = StringField(verbose_name="Code")
    color = StringField(verbose_name="Color", null=True)

class Product(Document):
    name = StringField(max_length=100, unique=True, required=True)
    description = StringField(max_length=255, null=True)
    product_group = ReferenceField('ProductGroup', required=True)
    detail = EmbeddedDocumentField('ProductDetail')

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
