from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from .models import Drama, Episode, Genre
from django.core.paginator import Paginator

# Create your views here.
genres = Genre.objects.all()
# SITEINFO
Sitename = "DramaLynk"
site_desc = "Normal Site description"


def index(request):
    dramas = Drama.objects.all().order_by('-pub_date')
    paginator = Paginator(dramas, 12)
    page_number = request.GET.get('page')
    latest_drama = paginator.get_page(page_number)
    pages = paginator.page_range
    geturl = request._current_scheme_host + request.path
    context = {
        'title': 'D&MLynk',
        'latest_drama': latest_drama,
        'pages': pages,
        'genres': genres,
        'geturl': geturl,
        'Sitename': Sitename,
        'site_desc': site_desc
    }
    return render(request, 'index.html', context)


def details(request, slug):
    try:
        drama = Drama.objects.get(slug=slug)
    except Drama.DoesNotExist:
        drama = None

    dramas = Drama.objects.all().order_by('-pub_date')[:15]
    geturl = request._current_scheme_host + request.path

    episodes = Episode.objects.filter(drama=drama)

    context = {
        'drama': drama,
        'dramas': dramas,
        'episodes': episodes,
        'genres': genres,
        'geturl': geturl,
        'Sitename': Sitename,
    }

    return render(request, 'details.html', context)


def genrePage(request, name):
    try:
        genre = Genre.objects.get(name=name)
    except Genre.DoesNotExist:
        genre = None

    dramas = Drama.objects.filter(genre=genre)
    geturl = request._current_scheme_host + request.path
    context = {
        'dramas': dramas,
        'genre': genre,
        'genres': genres,
        'geturl': geturl,
        'Sitename': Sitename,
        'site_desc': site_desc
    }

    return render(request, 'genre.html', context)


def episode_detail(request, ep_slug):
    episode = Episode.objects.get(ep_slug=ep_slug)
    episodes = Episode.objects.filter(drama=episode.drama)
    geturl = request._current_scheme_host + request.path
    context = {'episode': episode, 'genres': genres,
               'episodes': episodes, 'geturl': geturl, 'Sitename': Sitename}

    return render(request, 'episode.html', context)


def searchPage(request):
    query = request.GET.get("q")
    drama_list = Drama.objects.filter(
        Q(title__icontains=query) | Q(title__icontains=query))

    geturl = request._current_scheme_host + request.path
    getpath = request.path

    context = {
        'drama_list': drama_list,
        'genres': genres,
        'geturl': geturl,
        'Sitename': Sitename,
        'getpath': getpath,
        'site_desc': site_desc
    }

    return render(request, 'search.html', context)
