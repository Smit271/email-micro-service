from django.contrib import admin
from send_email_app.models import APIKeyModel, EmailLogs

admin.site.register(APIKeyModel)
admin.site.register(EmailLogs)
