# core/admin.py

from django.contrib import admin
from .models import Demanda

class DemandaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_demanda', 'is_concluded')  # Remova 'criado_por' se estiver presente
    list_filter = ('is_concluded', 'data_demanda')
    search_fields = ('titulo', 'descricao')

admin.site.register(Demanda, DemandaAdmin)
