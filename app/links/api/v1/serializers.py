from typing import Any, Dict

from rest_framework import serializers

from links.models import Link, Collection
from links.service_links import ServiceLink


class LinkSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    links = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=Link.objects.all()),
        required=False
    )

    class Meta:
        model = Link
        fields = '__all__'

    def create(self, validated_data: Dict[str, Any]) -> Link:
        url = validated_data.pop('url')
        parsed_data = ServiceLink.parse_link(url)

        link = Link(
            title=parsed_data['title'],
            description=parsed_data['description'],
            url=url,
            preview_image=parsed_data['preview_image'],
            link_type=parsed_data['link_type'],
            owner=validated_data.get('owner')
        )
        link.save()
        return link


class CollectionSerializer(serializers.ModelSerializer):
    links = serializers.PrimaryKeyRelatedField(
        queryset=Link.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Collection
        fields = [
            'id',
            'title',
            'description',
            'created_at',
            'updated_at',
            'owner',
            'links'
        ]
        read_only_fields = ['owner', 'created_date', 'updated_date']

    def create(self, validated_data: Dict[str, Any]) -> Collection:
        links = validated_data.pop('links', [])
        collection = Collection.objects.create(**validated_data)
        collection.links.set(links)
        return collection

    def update(self, instance: Collection, validated_data: Dict[str, Any]) -> Collection:
        links = validated_data.pop('links', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if links is not None:
            instance.links.set(links)
        instance.save()
        return instance
