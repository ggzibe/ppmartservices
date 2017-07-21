from rest_framework_mongoengine.serializers import DocumentSerializer
from product_group_app.models import ProductGroup
from product_type_app.serializers import ProductTypeSerializer

class ProductGroupSerializer(DocumentSerializer):
    class Meta:
        model = ProductGroup
        fields = '__all__'

class ProductGroupReadOnlySerializer(DocumentSerializer):
    product_type = ProductTypeSerializer(many=False, read_only=True)

    class Meta:
        model = ProductGroup
        fields = '__all__'
