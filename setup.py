# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from js_components import __version__

REQUIREMENTS = [
    'django-cms>=3.4.0',
    'django-filer>=1.2.4',
    'django-friendly-tag-loader==1.3.1',
    'djangocms-attributes-field>=0.1.1',
    'djangocms-text-ckeditor>=3.1.0',
    'twython==3.7.0',
    'python-dateutil',
]

setup(
    name='js-components',
    version=__version__,
    description=open('README.rst').read(),
    author='Compound Partners Ltd',
    author_email='hello@compoundpartners.co.uk',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False,
)
