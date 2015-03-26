from rest_framework import serializers
from db.models import Orders, OrdersDetails

__author__ = 'pluto'


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders


class OrdersDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrdersDetails