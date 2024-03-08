import uuid
from django.db import models


class APIKeyModel(models.Model):
    service_name = models.CharField(max_length=255)
    # For Which Service we are creating APIKey name
    api_key = models.UUIDField(
        default=uuid.uuid4, editable=False, db_index=True)
    is_expirable = models.BooleanField(default=False)
    expiry_date = models.DateField(null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'api_key_model'

    def __str__(self) -> str:
        return str(self.api_key)


class EmailLogs(models.Model):
    from_email = models.EmailField(null=True)
    to_email = models.TextField(null=True)
    api_key = models.ForeignKey(
        'APIKeyModel', on_delete=models.DO_NOTHING, null=True)
    subject = models.CharField(max_length=255)
    email_body = models.TextField(null=True)
    is_attachments = models.BooleanField(default=False)
    sent_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'email_logs'
