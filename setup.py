from setuptools import setup, find_packages


setup(
    name='cloudfiles',
    version='0.0.1',  # Modify in __init__.py as well
    url='https://github.com/piecommerce/django-cloudfiles',
    license='BSD',
    description='A (model-less) Django app providing a Rackspace(tm) Cloud '
                'Files(tm) storage backend',
    author='piecommerce',
    author_email='michael@piecommerce.com',
    packages=find_packages(where='.'),
    test_suite='cloudfiles.runtests.runtests.main',
    install_requires=['pyrax==1.4.5'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
