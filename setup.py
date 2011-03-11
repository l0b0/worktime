#!/usr/bin/env python
"""
Setup configuration
"""

from setuptools import find_packages, setup
from worktime import worktime as package

setup(
    name='worktime',
    version='0.3.1',
    description='Generate XHTML daily calendar',
    long_description=package.__doc__,
    url='http://github.com/l0b0/worktime',
    keywords='log calendar generator',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    include_package_data=True,
    entry_points={
        'console_scripts': ['worktime = worktime.worktime:main']},
    classifiers=[
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
    test_suite='tests.tests',
    author=package.__author__,
    author_email=package.__email__,
    maintainer=package.__maintainer__,
    maintainer_email=package.__email__,
    download_url='http://github.com/l0b0/worktime',
    platforms=['POSIX', 'Windows'],
    license=package.__license__,
    )
