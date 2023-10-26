# designs/admin.py
from django.contrib import admin
from .models import Design, Client

class DesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'designer', 'created_at')
    list_filter = ('designer',)
    search_fields = ('title', 'designer__username')
    prepopulated_fields = {'title': ('title',)}
    date_hierarchy = 'created_at'

class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferences')
    search_fields = ('user__username',)

admin.site.register(Design, DesignAdmin)
admin.site.register(Client, ClientAdmin)
