# -*- coding: utf-8 -*-
from django.conf import settings
from django import forms
from django.template import Context
from django.template.loader import get_template

from image_gallery.models import GalleryImage


class GalleryWidget(forms.HiddenInput):
    is_hidden = False

    class Media:
        css = {'all': ("%simage_gallery/css/image_gallery.css" % settings.STATIC_URL,)}
        js = ("%simage_gallery/js/image_gallery.js" % settings.STATIC_URL,
              "%simage_gallery/js/jquery.form.js" % settings.STATIC_URL,)

    def __init__(self, attrs=None):
        self.max_images = attrs.pop('max_images')
        super(GalleryWidget, self).__init__(attrs)

    def render(self, name, values, attrs=None):
        input_value = ','.join(str(x) for x in values) if values is not None else ''
        choise_input = super(GalleryWidget, self).render(name, input_value, attrs)
        final_attrs = self.build_attrs(attrs, name=name)
        id = final_attrs['id'] if final_attrs and 'id' in final_attrs else 'id-gallery'
        images = []
        if values:
            if type(values) != type([]):
                values = values.split(',')
            imgs = GalleryImage.objects.filter(id__in=values)
            for i in values:
                images.append({'id': i,
                              'src': imgs.get(id=i).thumbnail.url,
                              })
        t = get_template('image_gallery/gallery.html')
        return choise_input + t.render(Context({'id': id,
                                                'max_images': self.max_images,
                                                'images': images,
                                               }))
