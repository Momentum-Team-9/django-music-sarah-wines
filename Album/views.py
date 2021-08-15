from django.shortcuts import render, get_object_or_404
from .models import Album, Track
# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/list_albums.html', {'albums': albums})

def show_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(
        request,
        "albums/show_album.html",
        {"album": album, "pk": pk},
    )