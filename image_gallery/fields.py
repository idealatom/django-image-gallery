# -*- coding: utf-8 -*-
from django.db import models

from image_gallery.models import GalleryImage
from image_gallery.forms import GalleryFormField


class GalleryField(models.ManyToManyField):
    def __init__(self, **kwargs):
        self.max_images = kwargs.pop('max_images')
        super(GalleryField, self).__init__(GalleryImage, **kwargs)
        self.help_text = kwargs.get('help_text')

    def formfield(self, **kwargs):
        defaults = {'form_class': GalleryFormField,
                    'max_images': self.max_images, }
        defaults.update(kwargs)
        return super(GalleryField, self).formfield(**defaults)


from south.modelsinspector import add_introspection_rules
rules = [
    (
        (models.fields.files.ImageField),
        [],
        {
            "max_images": ["max_images", {"default": None}],
        },
    )
]
add_introspection_rules(rules, ["^image_gallery\.fields\.GalleryField"])
