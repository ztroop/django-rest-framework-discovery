from rest_framework import serializers

from api import models


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Property
        fields = "__all__"


class PropertyDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PropertyDetail
        fields = "__all__"


class EvaluationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Evaluation
        fields = "__all__"


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Location
        fields = "__all__"


class ZillowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Zillow
        fields = "__all__"
