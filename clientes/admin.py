from django.contrib import admin
from .models import Cliente
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cell_phone', 'email')
    search_fields = ('first_name', 'last_name')