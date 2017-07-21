from product_group_app.models import ProductGroup
from product_group_app.serializers import ProductGroupSerializer, ProductGroupReadOnlySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProductGroupListView(APIView):
    def get(self, request, format=None):
        try:
            queryset = ProductGroup.objects().all()
            serializer = ProductGroupReadOnlySerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise Http404

    def post(self, request, format=None):
        serializer = ProductGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductGroupDetailView(APIView):
    def get(self, request, pk, format=None):
        try:
            queryset = ProductGroup.objects.get(pk=pk)
            serializer = ProductGroupReadOnlySerializer(serializer)
            return Response(serializer.data)
        except Exception as e:
            raise Http404

    def put(self, request, pk, format=None):
        productgroup = ProductGroup.objects.get(pk=pk)
        serializer = ProductGroupSerializer(productgroup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def  delete(self, request, pk, format=None):
        productgroup = ProductGroup.objects.get(pk=pk)
        productgroup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
