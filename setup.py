#!/usr/bin/env python3

import sys
from setuptools import setup
from setuptools import find_packages


if sys.version_info[:3] < (3, 5):
    raise SystemExit("You need Python 3.5+")


setup(
    name="misoc",
    version="0.6.dev",
    description="a high performance and small footprint SoC based on Migen",
    long_description=open("README").read(),
    author="Sebastien Bourdeauducq",
    author_email="sb@m-labs.hk",
    url="https://m-labs.hk",
    download_url="https://github.com/m-labs/misoc",
    license="BSD",
    platforms=["Any"],
    keywords="HDL ASIC FPGA hardware design",
    classifiers=[
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Environment :: Console",
        "Development Status :: Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    packages=find_packages(),
    # install_requires=["pyserial", "asyncserial"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "flterm=misoc.tools.flterm:main",
            "mkmscimg=misoc.tools.mkmscimg:main",
        ],
    },
)
