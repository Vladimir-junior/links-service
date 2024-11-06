from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from users.api.v1.views import UserViewSet, TopUsersView
from links.api.v1.views import LinkViewSet, CollectionViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'links', LinkViewSet, basename='links')
router.register(r'collections', CollectionViewSet, basename='collections')

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="Description API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/top-users/', TopUsersView.as_view(), name='top-users'),
]
