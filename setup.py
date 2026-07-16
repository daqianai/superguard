##############################################################################
#
# Copyright (c) 2008-2013 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# Copyright (c) 2025-present Superguard Contributors.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os
import sys

py_version = sys.version_info[:2]

if py_version < (2, 7):
    raise RuntimeError("On Python 2, superguard requires Python 2.7 or later")
elif (3, 0) < py_version < (3, 4):
    raise RuntimeError("On Python 3, superguard requires Python 3.4 or later")

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, "README.rst")).read()
except (IOError, OSError):
    README = ""
try:
    CHANGES = open(os.path.join(here, "CHANGES.md")).read()
except (IOError, OSError):
    CHANGES = ""

setup(
    name="superguard",
    version="0.0.2",
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    description="Modern health check and process monitoring toolkit for supervisord",
    long_description=README + "\n\n" + CHANGES,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: System :: Boot",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
    ],
    author="Superguard Contributors",
    author_email="wcxontheway@126.com",
    url="https://github.com/daqianai/superguard",
    keywords="supervisor monitoring health-check process-management",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "supervisor",
    ],
    extras_require={
        "test": ["pytest"],
    },
    test_suite="superguard.tests",
    entry_points="""\
      [console_scripts]
      httpok = superguard.httpok:main
      crashsms = superguard.crashsms:main
      crashmail = superguard.crashmail:main
      crashmailbatch = superguard.crashmailbatch:main
      fatalmailbatch = superguard.fatalmailbatch:main
      memmon = superguard.memmon:main
      """,
)
