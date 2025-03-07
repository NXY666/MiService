#!/usr/bin/env python3
import os
import sys

if len(sys.argv) == 1:
    os.system('%s sdist' % sys.argv[0])
    os.system('rm -rf dist *.egg-info')
    exit(0)

from pathlib import Path

from setuptools import setup

from micli import MISERVICE_VERSION

setup(
    name='miservice',
    description='XiaoMi Cloud Service',
    version=MISERVICE_VERSION,
    license='MIT',
    author='Yonsm',
    author_email='Yonsm@qq.com',
    url='https://github.com/NXY666/MiService',
    long_description=Path('README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    packages=['miservice'],
    scripts=['micli.py'],
    python_requires='>=3.7',
    install_requires=['aiohttp'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
