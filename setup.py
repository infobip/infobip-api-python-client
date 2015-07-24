#!/usr/bin/python

# Copyright 2015 Infobip
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import distutils.core as mod_distutilscore

from setuptools import find_packages

# Try to parse README.md and convert it to rst format
# which can be used on PyPi. Using Pandoc & PyPandoc.
try:
    import pypandoc
    long_description = '\n\n' + pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = '\n\n' + open('README.md').read()

# Properly register all python source files from package
my_packages = find_packages()

mod_distutilscore.setup(
    name='infobip-api-python-client',
    version='0.1.2',
    description='Infobip SMS API client library in Python',
    long_description=long_description,
    license='Apache License, Version 2.0',
    author='Infobip Ltd. - Plugins Team (SMS API client)',
    author_email='plugins@infobip.com',
    maintainer='Infobip Ltd. - Plugins Team (SMS API client)',
    maintainer_email='plugins@infobip.com',
    url='https://github.com/infobip/infobip-api-python-client',
    packages=my_packages,
    package_dir={'infobip_api_python_client': 'infobip_api_python_client'},
    keywords=[
        'infobip',
        'sms',
        'api',
        'msisdn'
    ],
    classifiers=[
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications :: Telephony",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Development Status :: 4 - Beta"
    ]
)
