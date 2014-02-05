0.2.3 (09.12.2013)
******************

* changed default added in 0.2.2 for generated urls to use https rather than http
* allow creating write-once files, by setting replace=False on upload
* override Storage.get_available_name to stop creating extra files when you intended to replace existing file.
* by default will now replace existing files rather than creating a new file with suffix
* tidy up duplicate code in shortcuts
* reduce the default expire period to 30 seconds


0.2.2 (08.12.2013)
******************

* allow using s3 based storage not hosted by Amazon
* added more shortcut functions (delete, get_url, download)
* allow to set permissions on bucket/key other than 'public-read'
* fixed S3Storage.url
* hopefully all backwards compatible

0.2.1 (03.08.2013)
******************

* fixed file saving bug (thanks @loweroctave)

0.2 (02.08.2013)
****************

* Upgraded upload shortcut to use custom filename (thanks @ivan-yurin)

0.1.6b (23.04.2012)
*******************

* fixed returned url

0.1.5b (23.04.2012)
*******************

* key uploading exception wrapped to IOError exception and added message

0.1.4b (21.04.2012)
*******************

* Seek(0) saved file before save

0.1.3b (21.04.2012)
*******************

* Fixed S3Storage._save
* Fixed S3Storage.__init__
* Fixed upload shortcut

0.1.2b (21.04.2012)
*******************

* Fixed S3Storage._save

0.1.1b (18.04.2012)
*******************

* Fixed S3Storage.listdir
* Fixed README.

0.1b (18.04.2012)
*****************

* S3 backend for django file storage
