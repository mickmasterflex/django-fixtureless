from distutils.core import setup

version = '0.6.0'

LONG_DESCRIPTION = """
=====================================
django-fixtureless
=====================================

fixtureless provides an easy way to create model objects within your Django
project for testing purposes.  This is done through inspection of your
database relationships.  All required fields are randomly filled.
All foreign key relationships will create respective objects in the
same fashion.

.. note:: django-fixtureless only supports Django 1.4 or higher and Python
2.7.x and Python 3.3.x.

.. _Django: http://djangoproject.com
"""

setup(
    name='django-fixtureless',
    version=version,
    author='Rico Cordova',
    author_email='rico.cordova@rocksolidbox.com',
    packages=['fixtureless'],
    url='https://github.com/ricomoss/django-fixtureless',
    license='LICENSE',
    description='fixtureless testing utility',
    long_description=LONG_DESCRIPTION,
    keywords='unittest,django',
    install_requires=['django >= 1.4'],
)
