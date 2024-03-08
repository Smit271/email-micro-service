from rest_framework import serializers

class SendSimpleMailSerializer(serializers.Serializer):
    from_email = serializers.EmailField()
    to_email = serializers.ListField()
    subject = serializers.CharField()
    email_body = serializers.CharField()
    is_attachments = serializers.BooleanField(default=False)
    
    