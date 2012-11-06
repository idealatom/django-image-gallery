from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from image_gallery.widgets import GalleryWidget


class GalleryFormField(forms.ModelMultipleChoiceField):
    default_error_messages = {
        'image_count': (_(u'Too many images'))
    }

    def __init__(self, queryset, cache_choices=False, required=True,
                     widget=None, label=None, initial=None,
                     help_text=None, *args, **kwargs):
        self.max_images = kwargs.pop('max_images')
        widget = GalleryWidget(attrs={'max_images': self.max_images, })
        super(GalleryFormField, self).__init__(queryset,
                cache_choices, required, widget, label, initial, help_text,
                *args, **kwargs)

    def clean(self, value):
        value = value.split(',') if value else []
        if self.max_images and len(value) > self.max_images:
            raise ValidationError(self.error_messages['image_count'])
        return super(GalleryFormField, self).clean(value)
