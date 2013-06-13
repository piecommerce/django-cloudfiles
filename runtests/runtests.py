import os
import sys

from django.core.management import call_command


# Prepend the top dir herein to sys.path for Django's DiscoverRunner
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))


def main():
    """
    Adds Django settings module environment variable, runs tests, exits.
    """
    # Add the Django settings module environment variable
    os.environ['DJANGO_SETTINGS_MODULE'] = 'runtests.settings'
    call_command('test', 'cloudfiles_app')


# When in main
if __name__ == '__main__':
    main()
