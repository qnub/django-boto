# -*- coding: utf-8 -*-

import string
import random
import logging
import urllib2
from os import path

from django.test import TestCase
from django.core.files.base import ContentFile

from s3 import upload
from s3.storage import S3Storage
from settings import BOTO_S3_BUCKET

logger = logging.getLogger(__name__)

local_path = path.realpath(path.dirname(__file__))


def get_string(lngth):
    strn = ''

    for i in xrange(lngth):
        strn += random.choice(string.letters)

    return strn


class BotoTest(TestCase):
    """
    Testing Amazon S3.
    """

    def test_storage(self):
        """
        Storage testing.
        """
        text = ''
        storage = S3Storage(host='s3.amazonaws.com')

        file_length = random.randrange(300, 1300)
        text = get_string(file_length)

        filename_length = random.randrange(5, 12)
        filename = get_string(filename_length)

        self.assertFalse(storage.exists(filename))

        test_file = ContentFile(text)
        test_file.name = filename
        uploaded_url = upload(test_file, host='s3.amazonaws.com')

        self.assertTrue(storage.exists(filename))

        url = 'http://' + BOTO_S3_BUCKET + '.s3.amazonaws.com/' + filename
        self.assertEqual(uploaded_url, url)

        page = urllib2.urlopen(uploaded_url)

        self.assertEqual(text, page.read())
        self.assertEqual(len(text), storage.size(filename))
        self.assertEqual(url, storage.url(filename))

        storage.delete(filename)
        self.assertFalse(storage.exists(filename))
