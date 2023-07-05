from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup


@admin.register(MenuLink)  # registar o admin
class MenuLinkAdmin(admin.ModelAdmin):
    # listar campos que vão aparecer
    list_display = 'id', 'text', 'url_or_path'
    # colocar links nas entradas
    list_display_links = 'id', 'text', 'url_or_path'
    # por que campos queremos buscar
    search_fields = 'id', 'text', 'url_or_path'


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',

    # o utilizador só pode criar 1 setup. Se já exixtir desaparece o adicionar
    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
