

import re
import os

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="django-Harman",
    version="1.1.0",
    description="Super awesome portable module for Django",
    long_description="Here you can elaborate a bit to explain the use case and purpose of the module.",
    author="Harman Kibue",
    author_email="harmannkibue@gmail.com",
    url="https://github.com/harmannkibue/Django_harmanModule",
    download_url="https://github.com/harmannkibue/Django_harmanModule.git",
    license="MIT License",
    packages=[
        "django_Harman",
    ],
    include_package_data=True,
    install_requires=[
        "Django>=1.7.0",
    ],
    tests_require=[
        "nose",
        "coverage",
    ],
    zip_safe=False,
    test_suite="tests.runtests.start",
    classifiers=[
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)