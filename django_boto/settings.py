# -*- coding: utf-8 -*-

from django.conf import settings


AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY

BOTO_S3_BUCKET = getattr(settings, 'BOTO_S3_BUCKET',
    AWS_ACCESS_KEY_ID.lower()).lower()

BOTO_S3_HOST = getattr(settings, 'BOTO_S3_HOST', 's3.amazonaws.com')

BOTO_BUCKET_LOCATION = getattr(settings, 'BOTO_BUCKET_LOCATION', 'DEFAULT')
