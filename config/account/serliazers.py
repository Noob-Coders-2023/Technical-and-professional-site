from rest_framework import serializers
from account.models import OTPRequest


class RequestOtpSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=20, allow_null=False)
    PHONE = serializers.CharField(allow_null=False)


class RequestOTPResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=OTPRequest
        fields=['request_id']