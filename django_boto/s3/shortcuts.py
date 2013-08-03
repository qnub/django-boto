# -*- coding: utf-8 -*-

from django.core.files import File
from storage import S3Storage


def upload(filename, name=None, prefix=False, bucket_name=False, key=None,
           secret=None, host=None):
    """
    Uploading files to Amamzon S3.
    """
    if isinstance(filename, basestring):
        fl = open(filename, 'rb')
    elif isinstance(filename, (file, File)):
        fl = filename
    else:
        raise TypeError('File must be file or string instance.')

    if not name:
        name = fl.name

    if prefix:
        if prefix.endswith('/'):
            full_path = prefix + name
        else:
            full_path = prefix + '/' + name
    else:
        full_path = name

    s3 = S3Storage(bucket_name=bucket_name, key=key, secret=secret, host=host)
    s3.save(full_path, fl)

    return s3.url(full_path)
