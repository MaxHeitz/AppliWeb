from django.http import Http404
from django.shortcuts import render
from .models import Album, Track


def home(request):
    """On affiche la liste des albums"""
    albums = Album.objects.all()
    return render(request, 'list.html', {'albums': albums})


def info_album(request, id_album):
    albums = Album.objects.all()
    album = Album.objects.get(id=id_album)
    tracks = Track.objects.filter(album=album)
    return render(request, 'info_album.html', locals())

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

    return render(request, 'list.html', {'albums':albums})
