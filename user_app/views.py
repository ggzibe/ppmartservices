from mongoengine.django.auth import User
from user_app.serializers import UserSerializer
from django.http import Http404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from auth_app.authentication import MongoTokenAuthentication

class UserList(APIView):
    authentication_classes = (MongoTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@authentication_classes((MongoTokenAuthentication))
@permission_classes((IsAuthenticated,))
def myuser(request, pk):
    try:
        user = User.objects.get(username=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@authentication_classes((MongoTokenAuthentication))
@permission_classes((IsAuthenticated,))
def delete(request, pk):
    try:
        user = User.objects.get(username=pk)
        user.delete()
        return Response({'message': 'delete completed.'})
    except Exception:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
