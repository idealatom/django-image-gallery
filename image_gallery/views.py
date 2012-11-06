# -*- coding: utf-8 -*-
import imghdr
import json
import os

from django.core.files import File
from django.http import HttpResponse
from django.views.generic.base import View
from django.utils.translation import ugettext as _
from PIL import Image

from image_gallery import settings
from image_gallery.models import GalleryImage

from utils import change_form_filenames
from utils import sizeof_fmt


class Upload(View):
    def post(self, request):
        response = {'success': False, }
        img = None
        if request.user.is_authenticated() or not settings.GALLERY_LOGIN_REQUIRED:
            file = (change_form_filenames(request.FILES)).get('image_gallery-file')
            if file:
                img = GalleryImage()
                img.image = file
                if request.user.is_authenticated():
                    img.owner = request.user
                img.save()

                img.thumbnail.save(os.path.basename(img.image.path), File(open(img.image.path)))
                thumb = Image.open(img.image.path)
                (w, h) = thumb.size
                side = min(w, h)
                thumb = thumb.crop([(w - side) / 2, (h - side) / 2, (w + side) / 2, (h + side) / 2])
                thumb.thumbnail(settings.GALLERY_THUMBNAILS_SIZE, Image.ANTIALIAS)
                thumb.save(img.thumbnail.path, quality=100)
                img.save()

                fsize = img.image.size
                max_fsize = settings.GALLERY_MAX_FILE_SIZE
                if fsize <= max_fsize:
                    type = imghdr.what(img.image.path).upper()
                    allowed_types = settings.GALLERY_IMAGE_TYPES
                    if type in allowed_types:
                        pil_img = Image.open(img.image.path)
                        min_size = settings.GALLERY_MIN_IMAGE_SIZE
                        max_size = settings.GALLERY_MAX_IMAGE_SIZE
                        if pil_img.size[0] >= min_size[0] and pil_img.size[1] >= min_size[1]:
                            if pil_img.size[0] <= max_size[0] and pil_img.size[1] <= max_size[1]:
                                response['success'] = True
                                response['id'] = img.id
                                response['url'] = img.thumbnail.url
                            else:
                                response['message'] = _('Maximal image size is %(w)sx%(h)s (Your image size is %(w_)sx%(h_)s).') % {'w': max_size[0], 'h': max_size[1], 'w_': pil_img.size[0], 'h_': pil_img.size[1]}
                        else:
                            response['message'] = _('Minimal image size is %(w)sx%(h)s (Your image size is %(w_)sx%(h_)s).') % {'w': min_size[0], 'h': min_size[1], 'w_': pil_img.size[0], 'h_': pil_img.size[1]}
                    else:
                        response['message'] = _('Unsupported image format. Supported formats are %s') % ', '.join(allowed_types).upper()
                else:
                    response['message'] = _('Maximal image file size is %s') % sizeof_fmt(max_fsize)
            else:
                response['message'] = _('Can not upload image. Please try again.')
        else:
            response['message'] = _('You must authorize to upload image.')

        if response['success'] == False and img is not None:
            img.delete()
        return HttpResponse(json.dumps(response))

#class Delete(View):
#    def post(self, request):
#        response = {'success':False }
#        id = request.POST.get('id')
#        if id:
#            img = GalleryImage.objects.get(id=id)
#            if img.owner == request.user or request.user.is_superuser:
#                img.delete()
#                response['success'] = True
#        return HttpResponse(json.dumps(response))
