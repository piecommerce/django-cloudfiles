import os
import sys


# Prepend the root dir herein to sys.path so that Django's DiscoverRunner
# doesn't find the tox-installed cloudfiles before finding the one herein
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))


def main():
    """
    Adds cloudfiles to sys.path, runs tests, exits.
    """
    # Add the Django settings module environment variable
    os.environ['DJANGO_SETTINGS_MODULE'] = 'cloudfiles.runtests.settings'

    from django.core.management import call_command

    call_command('test', 'cloudfiles')


# When in main
if __name__ == '__main__':
    main()
