
from django.urls import path
from send_email_app.views import (
    SendSimpleMailViewClass
)

urlpatterns = [
    path('send_simple_email', SendSimpleMailViewClass.as_view(),
         name='send_simple_email'),
]
