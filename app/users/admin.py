from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', )
    search_fields = ('email', )


admin.site.register(User, UserAdmin)
