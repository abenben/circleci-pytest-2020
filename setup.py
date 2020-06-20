"""Calclator project."""
  
from setuptools import setup, find_packages

setup(
    name='calclator',
    version='0.1.0',
    license='none',
    description='Calclator',

    author='Abenben',
    author_email='abenbenben@gmail.com',
    url='https://github.com/abenben/circleci-pytest-2020',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=[],
    extras_require={},

    entry_points={
        'console_scripts': [
            'calclator = calclator',
        ]
    },
)
