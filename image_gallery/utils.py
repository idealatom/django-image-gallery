import os
import hashlib
from datetime import datetime


def sizeof_fmt(num):
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')


def change_form_filenames(FILES):
    for i in FILES:
        fname, extension = os.path.splitext((FILES[i]).name)
        hsh = hashlib.md5()
        hsh.update(fname + str(datetime.now()))
        (FILES[i]).name = hsh.hexdigest()[0:15] + extension
    return FILES
