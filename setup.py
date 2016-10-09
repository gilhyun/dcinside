#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'cssselect',
    'fake-factory',
    'future',
    'lxml',
    'pyquery',
    'python-dateutil',
    'requests',
    'six'

]


test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='dcinside',
    version='0.1.0',
    description="Python Unofficial API for Dcinside.",
    long_description=readme + '\n\n' + history,
    author="carcdrcons",
    author_email='simple-is-better-than-complex@carcdrcons.com',
    url='https://github.com/carcdrcons/dcinside',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='dcinside',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
