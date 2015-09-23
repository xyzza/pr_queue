# coding: utf-8
from rest_framework import serializers
from developers.models import AllDevelopers, ProductQueue, DevelopersQueue


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AllDevelopers
        fields = ('name', 'email', 'is_active', 'pk')


class DevelopersQueueSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DevelopersQueue
        fields = ('name',)


class ProductQueueSerializer(serializers.HyperlinkedModelSerializer):

    dev_queue = serializers.HyperlinkedRelatedField(
        view_name='product-dev-queue', format='html', many=True, read_only=True)

    class Meta:
        model = ProductQueue
        fields = ('name', 'dev_queue', 'receivers')