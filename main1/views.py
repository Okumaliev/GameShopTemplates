from django.shortcuts import render

from main1.models import Game, Type
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    types = Type.objects.all()

    return render(request, 'main/index.html', {'types': types})


def game_list(request, slug):
    games = Game.objects.filter(type__slug=slug)
    types = Type.objects.all()
    print(games)
    page = request.GET.get('page', 1)
    paginator = Paginator(games, 1)
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

    return render(request, 'main/game_list.html',
                  {'games': games,
                   'types': types})


# def category_detail(request, slug):
#     categories = Type.objects.order_by('pk')
#     categorн = Type.objects.get(slug=slug)
#     games = Game.objects.filter(genre__slug=slug)
#     paginator = Paginator(games, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'game_list.html', locals())

