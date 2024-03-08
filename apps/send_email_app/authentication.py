from datetime import datetime, timedelta

from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError

from send_email_app.models import APIKeyModel


class CustomAPIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Extract the JWT from the Authorization header
        api_key = request.META.get('HTTP_AUTHORIZATION')
        print("===> api_key: ", api_key)
        if api_key is None:
            raise AuthenticationFailed(
                'API Key is required to call this service.')

        api_key = CustomAPIKeyAuthentication.get_the_token_from_header(
            api_key
        )  # clean the token
        try:
            api_obj = APIKeyModel.objects.filter(
                api_key=api_key,
                is_deleted=False
            ).first()

            if not api_key:
                raise AuthenticationFailed('API Key not valid')
        except:
            raise AuthenticationFailed('API Key is not valid')

        # Checking if API key is expired
        if api_obj.is_expirable and api_obj.expiry_date < datetime.today().date():
            raise AuthenticationFailed(
                'API Key is expired, please generate api key again from admin portal.'
            )

        # Return the user and token payload
        return api_obj, api_key

    def authenticate_header(self, request):
        return 'Token'

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Token', '').replace(' ', '')  # clean the token
        return token
