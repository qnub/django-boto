# -*- coding: utf-8 -*-

from django.core.files import File
from .storage import S3Storage


def upload(filename, name=None, prefix=False, bucket_name=False, key=None,
           secret=None, host=None, expires=30, query_auth=False, force_http=False,
           policy=None, replace=True):
    """
    Uploading files to Amamzon S3.
    Returns String.
    """
    if isinstance(filename, str):
        fl = open(filename, 'rb')
    elif isinstance(filename, File):
        fl = filename
    else:
        raise TypeError('File must be file or string instance.')

    if not name:
        name = fl.name

    full_path = _get_name(name, prefix)

    s3 = S3Storage(bucket_name=bucket_name, key=key, secret=secret, host=host,
                   policy=policy, replace=replace)
    s3.save(full_path, fl)

    return s3.url(full_path, expires, query_auth, force_http)


def get_url(name=None, prefix=False, bucket_name=False, key=None,
            secret=None, host=None, expires=30, query_auth=False, force_http=False):
    """
    Get Url for key on Amazon S3.
    Returns String.
    """
    full_path = _get_name(name, prefix)

    s3 = S3Storage(bucket_name=bucket_name, key=key, secret=secret, host=host)

    return s3.url(full_path, expires, query_auth, force_http)


def download(name=None, prefix=False, bucket_name=False, key=None,
             secret=None, host=None):
    """
    Download file from Amazon S3.
    Returns TemporaryFile().
    """
    full_path = _get_name(name, prefix)

    s3 = S3Storage(bucket_name=bucket_name, key=key, secret=secret, host=host)

    return s3.open(full_path)


def remove(name=None, prefix=False, bucket_name=False, key=None,
           secret=None, host=None):
    """
    Deletes file from Amazon S3.
    """
    full_path = _get_name(name, prefix)

    s3 = S3Storage(bucket_name=bucket_name, key=key, secret=secret, host=host)

    s3.delete(full_path)


def _get_name(name, prefix):

    if prefix:
        if prefix.endswith('/'):
            full_path = prefix + name
        else:
            full_path = prefix + '/' + name
    else:
        full_path = name

    return full_path
