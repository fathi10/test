from django.shortcuts import render
from articles.models import produit
# Create your views here.
def accueil(request):
    content = {'nom': produit.nom,
               'prix': produit.prix
               }
    return render(request, 'accueil/accueil.html', content)



def echange(request):
    content: {'title': 'LOGILAN MAROC',
    }
    return render(request, 'accueil/echange.html', content)


def inscription(request):
    content: {'title': 'LOGILAN MAROC',
    }
    return render(request, 'accueil/inscription.html', content)


def tablebord(request):
    content: {'title': 'LOGILAN MAROC',
    }
    return render(request, 'accueil/tablebord.html', content)


def login(request):
    content: {'title': 'LOGILAN MAROC',
    }
    return render(request, 'accueil/login.html', content)