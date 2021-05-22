#!/usr/bin/env python3
"""
pikepdf_annotations - PikePDF helper utilities

MIT License

Copyright (c) 2021 Damian Zaremba

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from pathlib import Path

import pkg_resources
from setuptools import setup, find_packages

with Path('README.md').open('r') as fh:
    long_description = fh.read()

with Path('requirements.txt').open('r') as fh:
    install_requires = [str(req) for req in pkg_resources.parse_requirements(fh)]

setup(
    name='pikepdf_annots',
    description='PikePDF helper utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DiveWithDamian/pikepdf-annots',
    packages=find_packages(),
    author='Damian Zaremba',
    author_email='oss@divewithdamian.eu',
    license='MIT',
    test_suite='tests',
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    keywords='pikepdf pdf annots annotations',
)
