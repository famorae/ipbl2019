from django.conf.urls import url
from django.template.response import TemplateResponse
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import SimpleRouter

from api.views import SampleViewSet
from api.views import index

router = SimpleRouter(trailing_slash=False)
router.register(r'sample', SampleViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Sample API",
        default_version='v1',
        description="Sample",
        contact=openapi.Contact(email="gustavo.gomides7@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    validators=['flex', 'ssv'],
    public=True,
)

urlpatterns = [
    url(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(
        cache_timeout=None), name='schema-json'),
    path('api/', include(router.urls)),
    path('sample', index, name='index'),
]
