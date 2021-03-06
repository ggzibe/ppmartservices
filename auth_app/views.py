from mongoengine.django.auth import User
from django.http import Http404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import MongoToken
from user_app.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from auth_app.authentication import MongoTokenAuthentication

@api_view(['POST'])
def login(request):
    result = {}
    try:
        user = User.objects.get(username = request.data['username'])
        if user.check_password(request.data['password']):
            user.backend = 'mongoengine.django.auth.MongoEngineBackend'
            token = MongoToken.objects.create(user=user)
            serializer = UserSerializer(user)
            result = {'result' : True, 'message': "Login completed.", 'data': {'user': serializer.data, 'token': token.key}}
        else:
            result = {'result' : False, 'message': "Incorrect password." }
        return Response(result)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes((MongoTokenAuthentication,))
@permission_classes((IsAuthenticated,))
def logout(request):
    try:
        token = MongoToken.objects.get(key=request.auth.key)
        token.delete()
        return Response('logout completed.')
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def createuser(request):
    result = {}
    try:
        if request.data['is_admin'] is True or request.data['is_admin'] == "true" or request.data['is_admin'] == "True":
            User.create_user(request.data['username'], request.data['password'], request.data['email'])
            user = User.objects.get(username = request.data['username'])
            user.is_superuser = True
            user.save()
        else:
            User.create_user(request.data['username'], request.data['password'], request.data['email'])
        result = {'result' : True, 'message': "Register completed."}
        return Response(result)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
