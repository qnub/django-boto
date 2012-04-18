# -*- coding: utf-8 -*-

from django.core.files.storage import Storage
from tempfile import TemporaryFile

from boto import connect_s3
from boto.s3.connection import Location
from boto.exception import S3CreateError
from django_boto import settings


class S3Storage(Storage):
    """
    Storage class.
    """

    def __init__(self, *args, **kwargs):
        bucket_name = kwargs.pop('bucket_name', settings.BOTO_S3_BUCKET)
        key = kwargs.pop('key', settings.AWS_ACCESS_KEY_ID)
        secret = kwargs.pop('secret', settings.AWS_SECRET_ACCESS_KEY)
        location = getattr(Location,
            kwargs.pop('location', settings.BOTO_BUCKET_LOCATION))
        self.s3 = connect_s3(key, secret)
        try:
            self.bucket = self.s3.create_bucket(bucket_name, location=location)
        except S3CreateError:
            self.bucket = self.s3.get_bucket(bucket_name)

        super(S3Storage, self).__init__(*args, **kwargs)

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

    def listdir(self, path):
        """
        Catalog file list.
        """
        return self.bucket.list(path, '/')

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
                settings.BOTO_S3_HOST + name
        else:
            return 'http://' + settings.BOTO_S3_BUCKET + '.' + \
                settings.BOTO_S3_HOST + '/' + name

    def _open(self, name, mode='rb'):
        """
        Open file.
        """
        result = TemporaryFile()
        self.bucket.new_key(name).get_file(result)

        return result

    def _save(self, name, content):
        """
        Save file.
        """
        key = self.bucket.new_key(name)
        key.set_contents_from_file(content)
        key.set_acl('public-read')

        return name

    def modified_time(self, name):
        """
        Last modification time.
        """
        return self.bucket.lookup(name).last_modified

    def path(self, name):
        """
        Local file path.
        """
        raise NotImplementedError

    def created_time(self, name):
        """
        Creation time.
        """
        raise NotImplementedError

    def accessed_time(self, name):
        """
        Last access time.
        """
        raise NotImplementedError
