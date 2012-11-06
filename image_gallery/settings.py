
from django.conf import settings

GALLERY_DIR = getattr(settings, 'GALLERY_DIR', 'image_gallery')
GALLERY_IMAGE_TYPES = getattr(settings, 'GALLERY_IMAGE_TYPES', ['GIF', 'JPEG', 'PNG'])
GALLERY_LOGIN_REQUIRED = getattr(settings, 'GALLERY_LOGIN_REQUIRED', False)
GALLERY_MAX_FILE_SIZE = getattr(settings, 'GALLERY_MAX_FILE_SIZE', 5 * 1024 * 1024)
GALLERY_MIN_IMAGE_SIZE = getattr(settings, 'GALLERY_MIN_IMAGE_SIZE', (100, 100))
GALLERY_MAX_IMAGE_SIZE = getattr(settings, 'GALLERY_MAX_IMAGE_SIZE', (2000, 3000))
GALLERY_THUMBNAILS_SIZE = getattr(settings, 'GALLERY_THUMBNAILS_SIZE', (100, 100))
