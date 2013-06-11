import pyrax

from django.conf import settings


class PyraxMixin(object):
    """
    A mixin class that provides access to the Rackspace Cloudfiles API.
    """
