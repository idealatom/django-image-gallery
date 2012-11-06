from django.contrib import admin
from image_gallery.models import *

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'creation_time')

admin.site.register(GalleryImage, GalleryImageAdmin)
