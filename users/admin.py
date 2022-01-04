from django.contrib import admin
from .models import API, Biodata

# Register your models here.

class BiodataAdmin(admin.ModelAdmin):
    list_display = ('user', 'nama', 'telp', 'alamat')
    search_fields = ('user', 'nama')

admin.site.register(Biodata, BiodataAdmin)

class APIAdmin(admin.ModelAdmin):
    list_display = ('user', 'api_key')
admin.site.register(API, APIAdmin)
