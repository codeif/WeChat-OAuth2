#!/usr/bin/env python
from setuptools import setup, find_packages
import re


with open('README.rst') as f:
    readme = f.read()

with open('wechat_oauth2/__about__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='wechat_oauth2',
    version='0.0.1',
    description='wechat sdk',
    long_description=readme,
    author='codeif',
    author_email='me@codeif.com',
    url='https://github.com/codeif/WeChat-OAuth2',
    license='BSD',
    install_requires=['rauth', 'requests'],
    packages=find_packages(),
)
