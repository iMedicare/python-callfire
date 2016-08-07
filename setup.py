#!/usr/bin/env python
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


setup(
    name='python-callfire',
    version='0.9.3',
    description='CallFire API thin wrapper.',
    long_description=readme,
    url='https://github.com/iMedicare/python-callfire',
    license=license,
    author='Alexander Shchapov',
    author_email='sasha@imedicare.com',
    install_requires=['six'],
    tests_require=['nose', 'flexmock'],
    test_suite='tests',
    packages=find_packages(exclude=('tests', 'swagger')),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ),
)

