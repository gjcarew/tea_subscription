from rest_framework import serializers
from subscriptions.models import Customer, Subscription


class CustomerSerializer(serializers.ModelSerializer):
    subscriptions = SubscriptionSerializer(many=True, read_only=True)
    class Meta:
        ordering = ['-id']
        model = Customer
        fields = ['id', 'fname', 'lname', 'email', 'subscriptions']
        extra_kwargs = {'books': {'required': False}}

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-id']
        model = Subscription
        fields = ['id', 'title', 'price', 'active', 'subscriptions']