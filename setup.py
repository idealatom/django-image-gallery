# -*- coding: utf-8 -*-
import os
from setuptools import setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name = "django-image-gallery",
    description = "Django ajax image gallery using jquery-forms and prettyPhoto",
    author = "Alexander Avdonin",
    author_email = "idealatom@gmail.com",
    url = "https://github.com/idealatom/django-image-gallery",
    version = "0.0.1",
    packages = ['image_gallery',
                'image_gallery.templatetags'],
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
)