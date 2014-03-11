#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from djangocms_styledlink import __version__


INSTALL_REQUIRES = [
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='djangocms-styledlink',
    version=__version__,
    description='Link Plugin for django CMS',
    author='Martin Koistinen',
    author_email='mkoistinen@gmail.com',
    url='https://github.com/mkoistinen/djangocms-styledlink',
    packages=['djangocms_styledlink', 'djangocms_styledlink.migrations'],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False
)