from django.contrib import admin

from .models import CollabUser

# Register your models here.
class CollabUserAdmin(admin.ModelAdmin):
	fields = ('email',)

admin.site.register(CollabUser, CollabUserAdmin)