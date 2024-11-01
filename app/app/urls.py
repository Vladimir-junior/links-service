from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.api.v1.views import (
    SignUpView,
    SignInView,
    PasswordResetView,
    LogOutView,
    ChangePasswordView)
from links.api.v1.views import LinkViewSet, CollectionViewSet

router = DefaultRouter()
router.register(r'links', LinkViewSet)
router.register(r'collections', CollectionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/sign-up/', SignUpView.as_view(), name='register'),
    path('api/v1/users/sign-in/', SignInView.as_view(), name='login'),
    path('api/v1/users/logout/', LogOutView.as_view(), name='logout'),
    path('api/v1/users/password_change/', ChangePasswordView.as_view(), name='password_change'),
    path('api/v1/users/password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/v1/users/', include(router.urls)),
]
