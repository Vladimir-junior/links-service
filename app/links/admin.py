from django.contrib import admin
from django.contrib.auth.models import User

from links.models import Link, Collection


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link_type', 'created_date', 'updated_date', 'url', 'owner')
    search_fields = ('title', )


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner', 'created_date', 'updated_date')
    search_fields = ('title', )


admin.site.register(Link, LinkAdmin)
admin.site.register(Collection, CollectionAdmin)

