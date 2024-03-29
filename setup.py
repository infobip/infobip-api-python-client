"""
    Infobip Client API Libraries OpenAPI Specification

    OpenAPI specification containing public endpoints supported in client API libraries.  # noqa: E501

    The version of the OpenAPI document: 1.0.172
    Contact: support@infobip.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "infobip-api-python-client"
VERSION = "3.0.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
]

# Try to parse README.md and convert it to rst format
# which can be used on PyPi. Using Pandoc & PyPandoc.
try:
    import pypandoc

    long_description = "\n\n" + pypandoc.convert("README.md", "rst")
except (IOError, ImportError):
    long_description = "\n\n" + open("README.md").read()

setup(
    name=NAME,
    version=VERSION,
    description="Infobip Client API Libraries OpenAPI Specification",
    author="Infobip Ltd.",
    author_email="support@infobip.com",
    url="https://github.com/infobip/infobip-api-python-client",
    keywords=[
        "infobip",
        "sms",
        "php",
        "tfa",
        "sdk",
        "rest",
        "api",
        "msisdn",
        "2fa",
        "openapi",
    ],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
    ],
)
