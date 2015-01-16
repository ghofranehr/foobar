#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for foobar.
"""

import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['-v']
        self.test_suite = True
    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

def parse_requirements(env='prod'):
    """load requirements from a pip requirements file"""
    tests_depends = [
        'pytest>=2.6.3',
        'pytest-cov==1.8.1',
        'WebTest==2.0.17',
        'factory-boy==2.4.1',
        'Flask-Script',
        'Flask-DebugToolbar==0.9.1'
    ]
    items = open('requirements/prod.txt').readlines()
    depends = [item.strip() for item in items if item.strip() and not item.startswith('#')]
    if (os.environ.get("PYTD_ENV") == 'test') or (env == 'test'):
        depends.extend(tests_depends)
    return depends

setup(
    name='foobar',
    version='1.0',
    description="A flasky application for terminologies search and translation.",
    url='https://github.com/ghofranehr/foobar',
    author='ghofranehr',
    author_email='ghofrane.hraghi@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': []},
    long_description=(README),
    license='GPLv2',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: GNU/Linux',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=parse_requirements(env='prod'),
    tests_require=parse_requirements(env='test'),
    cmdclass = {'test': PyTest},
    include_package_data=True,
)
