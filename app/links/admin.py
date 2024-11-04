from django.contrib import admin

from links.models import Link, Collection


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link_type', 'created_at', 'updated_at', 'url', 'owner')
    search_fields = ('title', )


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner', 'created_at', 'updated_at')
    search_fields = ('title', )


admin.site.register(Link, LinkAdmin)
admin.site.register(Collection, CollectionAdmin)

