from django.contrib import admin
from core.models import Evento, Contato, Endereco

class EventoAdmin(admin.ModelAdmin):
    list_display = ('contato', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('contato', 'data_evento')


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('contato', 'cep')

admin.site.register(Evento, EventoAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Endereco, EnderecoAdmin)
