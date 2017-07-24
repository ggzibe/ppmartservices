from rest_framework.authentication import TokenAuthentication
from .models import MongoToken
from rest_framework import exceptions

class MongoTokenAuthentication(TokenAuthentication):
    model = MongoToken
    def authenticate(self, request):
        try:
            if 'HTTP_AUTHORIZATION' in request.META:
                auth = request.META['HTTP_AUTHORIZATION']
                key = auth[6:]
                token = self.model.objects.get(key=key)
            else:
                raise exceptions.AuthenticationFailed('Authentication is Null')
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Unauthorized')
        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')
        return (token.user, token)
