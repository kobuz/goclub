from django.contrib import admin

from .models import Member


@admin.site.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'rank',)

