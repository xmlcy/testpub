#!/usr/bin/env python

from os import path
import re

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
version_file = path.join(here, "rena2_sdk_api", "__init__.py")

with open(version_file, "r") as f:
    version_match = re.search(r'__version__ = "(.*?)"', f.read())
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Version not found")


setup(
    name="rena2_sdk_api",
    version=version,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "grpcio==1.65.4",
        "grpcio-tools==1.65.4",
        "protobuf==5.29.4",
    ],
    author="Droid Robotics",
    description="gRPC Protobuf API definition for Rena 2 SDK",
)
