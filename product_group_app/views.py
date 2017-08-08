from product_group_app.models import ProductGroup
from product_group_app.serializers import ProductGroupSerializer, ProductGroupReadOnlySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from auth_app.authentication import MongoTokenAuthentication

# Create your views here.
class ProductGroupListView(APIView):
    authentication_classes = (MongoTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            queryset = ProductGroup.objects().all()
            serializer = ProductGroupReadOnlySerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        try:
            serializer = ProductGroupSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProductGroupDetailView(APIView):
    authentication_classes = (MongoTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        try:
            queryset = ProductGroup.objects.get(pk=pk)
            serializer = ProductGroupReadOnlySerializer(serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk, format=None):
        try:
            productgroup = ProductGroup.objects.get(pk=pk)
            serializer = ProductGroupSerializer(productgroup, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def  delete(self, request, pk, format=None):
        try:
            productgroup = ProductGroup.objects.get(pk=pk)
            productgroup.delete()
            return Response({'message': 'delete completed.'})
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
