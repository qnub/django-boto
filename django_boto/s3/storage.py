# -*- coding: utf-8 -*-

import logging

from django.core.files.storage import Storage
from tempfile import TemporaryFile

from boto import connect_s3
from boto.s3.connection import Location
from boto.exception import S3CreateError
from django_boto import settings


logger = logging.getLogger(__name__)


class S3Storage(Storage):
    """
    Storage class.
    """

    def __init__(self, bucket_name=None, key=None, secret=None, location=None,
        host=None):

        if not bucket_name:
            bucket_name = settings.BOTO_S3_BUCKET

        if not key:
            key = settings.AWS_ACCESS_KEY_ID

        if not secret:
            secret = settings.AWS_SECRET_ACCESS_KEY

        if not location:
            location = settings.BOTO_BUCKET_LOCATION

        if not host:
            host = settings.BOTO_S3_HOST

        self.host = host
        location = getattr(Location, location)
        self.s3 = connect_s3(key, secret)
        try:
            self.bucket = self.s3.create_bucket(bucket_name, location=location)
        except S3CreateError:
            self.bucket = self.s3.get_bucket(bucket_name)

    def delete(self, name):
        """
        Delete file.
        """
        self.bucket.new_key(name).delete()

    def exists(self, name):
        """
        Existing check.
        """
        return self.bucket.new_key(name).exists()

    def _list(self, path):
        result_list = self.bucket.list(path, '/')

        for key in result_list:
            yield key.name

    def listdir(self, path):
        """
        Catalog file list.
        """
        return [], self._list(path)

    def size(self, name):
        """
        File size.
        """
        return self.bucket.lookup(name).size

    def url(self, name):
        """
        URL for file downloading.
        """
        if name.startswith('/'):
            return 'http://' + settings.BOTO_S3_BUCKET + '.' + \
                self.host + name
        else:
            return 'http://' + settings.BOTO_S3_BUCKET + '.' + \
                self.host + '/' + name

    def _open(self, name, mode='rb'):
        """
        Open file.
        """
        result = TemporaryFile()
        self.bucket.get_key(name).get_file(result)

        return result

    def _save(self, name, content):
        """
        Save file.
        """
        key = self.bucket.new_key(name)

        key.set_contents_from_file(content)

        content.seek(0, 2)
        orig_size = content.tell()
        saved_size = key.size

        if saved_size == orig_size:
            key.set_acl('public-read')
        else:
            key.delete()

            raise IOError('Error during saving file %s - saved %s of %s bytes'
             % (name, saved_size, orig_size))

        return name

    def modified_time(self, name):
        """
        Last modification time.
        """
        return self.bucket.lookup(name).last_modified

    created_time = accessed_time = modified_time
