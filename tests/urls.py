from django.conf.urls import include, url

urlpatterns = [url(r'^api/', include('rest_framework_discovery.urls'))]
