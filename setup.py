#!/usr/bin/env python

from distutils.core import setup

setup(
        name = 'ckip',
        version = '0.1.2',
        description = 'CKIP chinese text segmentation Python API client ',
        author = 'Wei-Ning Huang',
        author_email = 'aitjcize@compose.ai',
        url = 'https://github.com/ComposeAI/pyCKIP',
        license = 'MIT',
        packages = ['ckip'],
        data_files = ['README.rst'],
        classifiers = [
            'Programming Language :: Python :: 2',
        ],
)
