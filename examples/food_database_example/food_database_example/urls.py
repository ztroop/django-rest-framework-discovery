from os import environ

from django.conf.urls import include, url
from django.views import generic
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^$', generic.RedirectView.as_view(
        url='/api/', permanent=False)),
    url(r'^api/food/', include('rest_framework_discovery.urls')),
    url(r'^api/', include_docs_urls(
        title=environ.get('APP_TITLE', 'API Docs'),
        authentication_classes=[],
        permission_classes=[],
    )),
]
