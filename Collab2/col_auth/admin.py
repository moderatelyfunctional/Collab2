from django.contrib import admin

from .models import CollabUser, Space

# Register your models here.
class CollabUserAdmin(admin.ModelAdmin):
	fields = ('email',)

class SpaceAdmin(admin.ModelAdmin):
	fields = ('url', 'participants', 'host')

admin.site.register(CollabUser, CollabUserAdmin)
admin.site.register(Space, SpaceAdmin)