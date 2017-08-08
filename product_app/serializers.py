from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from product_app.models import Product, ProductDetail

class ProductDetailSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'

class ProductSerializer(DocumentSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductReadOnlySerializer(DocumentSerializer):
    detail = ProductDetailSerializer(many=False)

    class Meta:
        model = Product
        fields = '__all__'
