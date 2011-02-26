#!/usr/bin/env python

from distutils.core import setup

setup(
    name="pants",
    version="0.9.5",
    description="A lightweight framework for writing asynchronous network applications in Python.",
    author="Christopher Davis",
    author_email="chris@wtfrak.com",
    url="http://pants.wtfrak.com/",
    download_url="https://bitbucket.org/ecdavis/pants/downloads/pants-0.9.5.zip",
    packages=["pants", "pants.contrib"],
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )