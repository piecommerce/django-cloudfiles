import os
import sys


def main():
    """
    Adds cloudfiles to sys.path, runs tests, exits.
    """
    # Add the Django settings module environment variable
    os.environ['DJANGO_SETTINGS_MODULE'] = 'cloudfiles.runtests.settings'

    from django.conf import settings
    from django.test.utils import get_runner

    # Get the test runner and run tests, exiting with the status codes set to
    # the result of the test running (num failures + num errors)
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    sys.exit(test_runner.run_tests(['cloudfiles']))


# When in main
if __name__ == '__main__':
    main()
