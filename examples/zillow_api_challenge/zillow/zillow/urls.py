from rest_framework import routers

from api import views
from django.conf.urls import include, url
from django.contrib import admin

router = routers.DefaultRouter()
router.register("property", views.PropertyViewSet, base_name="property")
router.register(
    "propertydetail", views.PropertyDetailViewSet, base_name="propertydetail"
)
router.register("zillow", views.ZillowViewSet, base_name="zillow")
router.register("location", views.LocationViewSet, base_name="location")
router.register("evaluation", views.EvaluationViewSet, base_name="evaluation")
urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^rest/v1/", include(router.urls)),
]
