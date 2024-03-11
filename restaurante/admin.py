from django.contrib import admin
from restaurante.models import Restaurante

# Register your models here.

class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao')
    list_display_links = ('id', 'titulo')


admin.site.register(Restaurante, RestauranteAdmin)
