from django.shortcuts import render
from articles.models import produit
from django.contrib import admin
# Create your views here.
def articles(request):
    content = {'nom': produit.nom,
               'title': 'Article',
               'prix': produit.prix
               }
    return render(request, 'articles/articles.html', content)


class Article(admin.ModelAdmin):
    list_display = ('nom','prix')
    articles.view_on_site = ()





