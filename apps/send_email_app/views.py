from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from send_email_app.authentication import CustomAPIKeyAuthentication
from send_email_app.serializers import SendSimpleMailSerializer


class SendSimpleMailViewClass(APIView):
    http_method_names = ['post',]
    authentication_classes = [CustomAPIKeyAuthentication]

    def post(self, request):
        context_data = dict()
        serializer_data = dict()

        serializer_data.update(
            **request.data
        )
        serializer_data['api_key'] = request.user.api_key

        serializer = SendSimpleMailSerializer(
            data=serializer_data
        )

        if serializer.is_valid():

            context_data['status'] = True
            context_data['message'] = "Mail Sent successfully."
            context_data['data'] = serializer.data

            return Response(context_data, status=status.HTTP_200_OK)
        else:
            error_message = ', '.join(
                [f"{key}: {', '.join(value)}" for key, value in serializer.errors.items()])

            context_data['status'] = False
            context_data['message'] = error_message
            context_data['data'] = {}

            return Response(context_data, status=status.HTTP_400_BAD_REQUEST)
