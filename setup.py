#!/usr/bin/env python
# encoding: UTF-8

import os
from setuptools import setup, find_packages
from setuptools.command.install import install as _install


class install(_install):
    def run(self):
        _install.run(self)
        # Additional setup if needed


long_description = ""

try:
    if os.path.isfile("README.rst"):
        long_description = open("README.rst", "r").read()
    elif os.path.isfile("README.md"):
        long_description = open("README.md", "r").read()
except Exception as error:
    print("Unable to read the README file: " + str(error))

setup(
    name="kattischeck",
    version="0.1",
    description="Test Kattis problems directly.",
    url="https://github.com/marcelroed/kattischeck",
    license="MIT",
    long_description=long_description,
    author="Marcel Rød",
    keywords="kattis test python cpp",
    platforms=["Windows"],
    packages=find_packages(),
    install_requires=[
        'urllib3>=1.24.1',
        'colorama>=0.4.1'
    ],
    entry_points={
        "console_scripts": [
            "kattis = kattischeck.__main__:main"
        ]
    },
    cmdclass={"install": install}
)
