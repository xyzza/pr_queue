# coding: utf-8
from rest_framework import serializers

from prqueue.developers.models import AllDevelopers, ProductQueue, DevelopersQueue


class DeveloperSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllDevelopers
        fields = ('pk', 'name', 'email', 'is_active')


class DevelopersQueueSerializer(serializers.ModelSerializer):

    developer = DeveloperSerializer(many=True)

    class Meta:
        model = DevelopersQueue
        fields = ('pk', 'name', 'developer')


class ProductQueueSerializer(serializers.ModelSerializer):

    dev_queue = DevelopersQueueSerializer(many=True)
    receivers = DeveloperSerializer(many=True)

    class Meta:
        model = ProductQueue
        fields = ('pk', 'name', 'dev_queue', 'receivers')