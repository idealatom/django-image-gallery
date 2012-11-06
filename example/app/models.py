from django.db import models

from image_gallery.fields import GalleryField


class Gallery(models.Model):
    author = models.CharField(max_length=20)
    gallery = GalleryField(max_images=5)
