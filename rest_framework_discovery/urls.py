from django.urls import path
from rest_framework import routers

from rest_framework_discovery.views import DiscoveryViewsets

router = routers.SimpleRouter()
viewsets = DiscoveryViewsets()

for table_name, viewset_class in viewsets.get_viewsets():
    router.register(table_name, viewset_class)

urlpatterns = [path('', viewsets.DiscoveryListView().as_view())] + router.urls
