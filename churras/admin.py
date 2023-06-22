from django.contrib import admin
from .models import Prato
# from pessoas.models import Pessoa
from django.contrib import admin


class ListandoPratos(admin.ModelAdmin):
    # nome_pessoa = Pessoa.nome 
    list_display = ('id','nome_prato','categoria','tempo_preparo', 'publicado') 
    list_display_links = ('id','nome_prato',) 
    search_fields = ('nome_prato',) 
    list_filter = ('categoria','publicado') 
    list_editable = ('publicado',) 
    list_per_page = 5


admin.site.register(Prato, ListandoPratos)

# Criar superusuario com o comando: manage.py createsuperuser