from mongoengine.django.auth import User
from user_app.serializers import UserSerializer
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserList(APIView):
    def get(self, request, format=None):
        try:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e))

@api_view(['GET'])
def myuser(request, pk):
    user = User.objects.get(username=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
    try:
        user = User.objects.get(username=pk)
        user.delete()
        return Response({'message': 'delete completed.'})
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
