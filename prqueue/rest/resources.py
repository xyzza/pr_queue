# coding: utf-8
from rest_framework import serializers, viewsets
from developers.models import AllDevelopers as Developer


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    """
    pass
    """
    class Meta:
        model = Developer
        fields = ('name', 'email', 'is_active')


class DeveloperViewSet(viewsets.ModelViewSet):
    """
    pass
    """
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer