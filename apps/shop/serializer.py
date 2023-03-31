from rest_framework import serializers


class GeneratePayLinkSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    amount = serializers.IntegerField()
