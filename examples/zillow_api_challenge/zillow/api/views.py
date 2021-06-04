from rest_framework import viewsets

from api import models, serializers


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertySerializer


class PropertyDetailViewSet(viewsets.ModelViewSet):
    queryset = models.PropertyDetail.objects.all()
    serializer_class = serializers.PropertyDetailSerializer


class ZillowViewSet(viewsets.ModelViewSet):
    queryset = models.Zillow.objects.all()
    serializer_class = serializers.ZillowSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer
