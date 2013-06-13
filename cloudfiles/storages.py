import pyrax
from pyrax.exceptions import (
    AuthenticationFailed,
    NoSuchContainer,
    NoSuchObject
)

from django.core.files.storage import DefaultStorage
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class CloudFilesStorage(DefaultStorage):
    """
    A Django storage backend that uses Rackspace Cloud Files to store files.
    """
    def __init__(self, options=None, *args, **kwargs):
        """
        Delegates to super, then attaches a pyrax cloud files connection.
        """
        # Transparent delegation to super
        super(CloudFilesStorage, self).__init__(*args, **kwargs)

        # Get cloudfiles settings, if options were not provided
        if options is None:
            try:
                options = settings.CLOUDFILES
            except AttributeError:
                raise ImproperlyConfigured(
                    u'Provide options or use settings.CLOUDFILES'
                )

        # Set pyrax authentication type to "rackspace" which is the one used
        # for the Rackspace "public cloud"
        pyrax.set_setting('identity_type', 'rackspace')

        # Set the encoding to utf-8 (default, but in the name explicitness)
        pyrax.set_setting('encoding', 'utf-8')

        # Get credentials
        try:
            username, api_key = options['USERNAME'], options['API_KEY']
        except KeyError:
            raise ImproperlyConfigured(
                u'USERNAME and API_KEY are both required options'
            )

        # Authenticate (accesses network)
        try:
            pyrax.set_credentials(username, api_key)
        except AuthenticationFailed:
            raise ImproperlyConfigured(
                u'Rackspace Cloudfiles API authentication failed - check '
                'username and api_key'
            )

        # Get the region
        try:
            region = options['REGION']
        except KeyError:
            raise ImproperlyConfigured(u'REGION is a required option')

        # Attach a cloudfiles connection for the selected region
        self.cloudfiles = pyrax.connect_to_cloudfiles(region=region)

        # Get the container name
        try:
            container = options['CONTAINER']
        except KeyError:
            raise ImproperlyConfigured(u'CONTAINER is a required option')

        # Attach the container
        try:
            self.container = self.cloudfiles.get_container(container)
        except NoSuchContainer:
            raise ImproperlyConfigured(
                u'No such container named "{c}"'.format(c=container)
            )

    def _save(self, name, content):
        """
        Stores the file to the attached container under the given name.
        """
        self.container.store_object(name, content)

    def delete(self, name, content):
        """
        Deletes the file under the given name from the attached container.
        """
        self.container.delete_object(name)

    def exists(self, name):
        """
        Returns whether or not a file under the given name exists in the
        attached container.
        """
        try:
            self.container.get_object(name)
        except NoSuchObject:
            return False

        return True

    def size(self, name):
        """
        Returns the size, in bytes, of the file stored under the given name.
        """
        return self.container.get_object(name).total_bytes

    def last_modified(self, name):
        """
        Returns the last modified time of the file stored under the given name.
        """
        return self.container.get_object(name).last_modified

    def url(self, name):
        """
        Returns the public URL for the file stored under the given name.
        """
        return u'/'.join([self.container.cdn_ssl_uri, name])
