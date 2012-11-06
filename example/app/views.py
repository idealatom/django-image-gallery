from django.views.generic import ListView
from django.views.generic.edit import CreateView

from models import Gallery


class GalleryList(ListView):
    model = Gallery


class AddGallery(CreateView):
    model = Gallery
    success_url = '/'
