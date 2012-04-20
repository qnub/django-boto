

Django-boto
===========

Is an implementation of django integration with **Amazon AWS**
(http://aws.amazon.com/) services trough **boto**
(https://github.com/boto/boto) module.

Installation
------------

To install::

    easy_install django-boto

or::

    pip install django-boto

Configuration
-------------

DEFAULT_FILE_STORAGE
********************

Can't be used as default file storage system because of ``path``
not implemented but you still can pass ``S3Storage`` object as storage option
to a ``FileField``::

    from django.db import models
    from django_boto.s3.storage import S3Storage

    s3 = S3Storage()

    class Car(models.Model):
        ...
        photo = models.ImageField(storage=s3)

Other settings.py options
*************************

``AWS_ACCESS_KEY_ID``
    *(rquired for default file storage using)* **Access Key ID** from
    **Security Credentials** settings on AWS service. Required for using
    as default storage.

``AWS_SECRET_ACCESS_KEY``
    *(rquired for default file storage using)* **Secret Access Key** from
    **Security Credentials** settings on AWS service. Required for using
    as default storage.

``BOTO_S3_BUCKET``
    Amazon S3 ``bucket`` name. Default set to ``AWS_ACCESS_KEY_ID``.

``BOTO_S3_HOST``
    Amazon S3 hostname. Default to ``s3.amazonaws.com``.

``BOTO_BUCKET_LOCATION``
    Amazon datacenter location. Default to ``US Classic Region``.

Using
-----

Default Django file storage
***************************

If set as default file storage - check for right set ``DEFAULT_FILE_STORAGE``,
``AWS_ACCESS_KEY_ID`` and ``AWS_SECRET_ACCESS_KEY`` in project ``settings.py``.

Manual S3Storage using
**********************

If need to using manually - you can direct set ``bucket_name``
(as ``BOTO_S3_BUCKET``), ``key`` (as ``AWS_ACCESS_KEY_ID``),
``secret`` (as ``AWS_SECRET_ACCESS_KEY``) and ``location``
(as ``BOTO_BUCKET_LOCATION``)
on storage instatiation::

    from boto.s3.storage import S3Storage

    s3 = S3Storage(bucket='another-bucket', key='another-key',
        secret='another-secret', location='EU')

``S3Storage`` - it's tipical `Djago storage system`_, only ``path``
is not implemented and ``created_time`` and ``accessed_time`` return
same value as ``modified_time``.

.. _Djago storage system: http://readthedocs.org/docs/django/en/1.4/ref/files/storage.html#the-storage-class:

Upload shortcut
***************

For simple uploading you can use shortcut::

    from django_boto.s3 import upload

    upload(filename, prefix=False, bucket_name=False, key=None, secret=None)

where:

``filename``
    ``string`` filesystem path to file or **django** ``File`` instance or
    **python** ``file`` object instance;
``prefix``
    ``string`` path prefix to filename in ``s3.amazonaws.com`` url. Like
    filename ``/images/image.jpg`` with ``avatars`` prefix convert to
    ``avatars/image.jpg`` in amazon url;
``bucket_name``
    name of bucket (if not exists - system try to create it) in amazon S3;
``key``
    ``AWS_ACCESS_KEY_ID`` replacement;
``secret``
    ``AWS_SECRET_ACCESS_KEY`` replacement.

It's retun URL for direct file download.

Last four options are optional. If not set - it takes from settings.py or
used defaults.
