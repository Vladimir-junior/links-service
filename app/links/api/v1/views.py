from rest_framework import viewsets, permissions
from rest_framework.serializers import Serializer

from links.models import Link, Collection
from links.api.v1.serializers import LinkSerializer, CollectionSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(owner=self.request.user)


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer: Serializer) -> None:
        serializer.save(owner=self.request.user)
