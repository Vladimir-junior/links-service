from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.api.v1.views import UserViewSet
from links.api.v1.views import LinkViewSet, CollectionViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'links', LinkViewSet, basename='links')
router.register(r'collections', CollectionViewSet, basename='collections')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

]
