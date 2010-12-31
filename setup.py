#!/usr/bin/env python
"""
Setup configuration
"""

from setuptools import find_packages, setup
from worktime.worktime import __author__ as module_author, __doc__ as module_doc, __email__ as module_email, __license__ as module_license, __maintainer__ as module_maintainer

setup(
    name = 'worktime',
    version = '0.3.1',
    description = 'Generate XHTML daily calendar',
    long_description = module_doc,
    url = 'http://github.com/l0b0/worktime',
    keywords = 'log calendar generator',
    packages = find_packages(exclude=['tests']),
    install_requires = [],
    include_package_data = True,
    entry_points = {
        'console_scripts': ['worktime = worktime.worktime:main']},
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Topic :: Office/Business',
        'Topic :: Other/Nonlisted Topic',
    ],
    test_suite = 'tests.tests',
    author = module_author,
    author_email = module_email,
    maintainer = module_maintainer,
    maintainer_email = module_email,
    download_url = 'http://github.com/l0b0/worktime',
    platforms = ['POSIX', 'Windows'],
    license = module_license,
    )
