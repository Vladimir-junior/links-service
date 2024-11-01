from django.db import models
from django.db.models import UniqueConstraint

from users.models import User
from links.api.v1.service_links import ServiceLink


class Link(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    preview_image = models.URLField(null=True, blank=True)
    link_type = models.CharField(
        max_length=20,
        choices=[('website', 'Website'),
                 ('book', 'Book'),
                 ('article', 'Article'),
                 ('music', 'Music'),
                 ('video', 'Video')
                 ],
        default='website'
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="links")

    class Meta:
        constraints = [
            UniqueConstraint(fields=['owner', 'url'], name='unique_user_link')
        ]

    def __str__(self):
        return self.title

    def fetch_link_data(self):
        data = ServiceLink.parse_link(self.url)
        self.title = data['title'] or self.title
        self.description = data['description'] or self.description
        self.preview_image = data['preview_image'] or self.preview_image
        self.link_type = data['link_type'] or self.link_type


class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collections")
    links = models.ManyToManyField(Link, related_name="collections")

    def __str__(self):
        return self.title
