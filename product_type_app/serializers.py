from rest_framework_mongoengine.serializers import DocumentSerializer
from product_type_app.models import ProductType

class ProductTypeSerializer(DocumentSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
