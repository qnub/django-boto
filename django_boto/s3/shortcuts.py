# -*- coding: utf-8 -*-

from os import path

from django.core.files import File
from storage import S3Storage


def upload(filename, prefix=False, bucket_name=False, key=None, secret=None,
    host=None):
    """
    Uploading files to Amamzon S3.
    """
    s3 = S3Storage(bucket_name=bucket_name, key=key, secret=secret, host=host)
    name = None

    if isinstance(filename, basestring):
        filename = open(filename, 'rb')
        name = path.basename(filename)
    elif isinstance(filename, (file, File)):
        name = filename.name

    if not name:
        raise TypeError('Filename must be file or string instance.')

    if prefix:
        if prefix.endswith('/'):
            full_path = prefix + name
        else:
            full_path = prefix + '/' + name
    else:
        full_path = name

    key = s3.save(full_path, filename)

    return s3.url(full_path)
