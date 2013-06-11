import pyrax

from django.conf import settings


class CloudFilesStorage(object):
    """
    A Django storage backend that uses Rackspace Cloud Files to store files.
    """
    # TODO: Finish this
