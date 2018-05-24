from django.contrib import admin
from articles.models import produit
# Register your models here.
admin.site.site_header = 'Logilan maroc administration'

class Article(admin.ModelAdmin):
    list_display = ('nom','prix')


admin.site.register(produit,Article)
