import os
from django.db import models
from django.contrib.auth.models import User

from image_gallery import settings


class GalleryImage(models.Model):

    image = models.ImageField(upload_to=settings.GALLERY_DIR)
    thumbnail = models.ImageField(upload_to=os.path.join(settings.GALLERY_DIR, 'thumbnails'))
    creation_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, blank=True, null=True)
