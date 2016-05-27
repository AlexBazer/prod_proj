from django.contrib import admin

from like.models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
