# -*- coding: utf-8 -*-

from os import path

from django.core.files import File
from django_boto import settings
from storage import S3Storage


def upload(filename, prefix=False, bucket_name=False, key=None, secret=None):
    """
    Uploading files to Amamzon S3.
    """
    if not bucket_name:
        bucket_name = settings.BOTO_S3_BUCKET

    if not key:
        key = settings.AWS_ACCESS_KEY_ID

    if not secret:
        secret = settings.AWS_SECRET_ACCESS_KEY

    s3 = S3Storage(bucket_name=bucket_name, key=key, secret=secret)
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
