from setuptools import setup

setup(
    name='transitsnake',
    version='0.0.2',
    url='https://github.com/otwartytransport/transitsnake',
    packages=['transitsnake', 'transitsnake.datasets'],
    license='Apache License 2.0',
    author='otwartytransport.pl and contributors',
    author_email='contact@otwartytransport.pl',
    description='Library for creating and reading GTFS files',
    install_requires=[
        'validators~=0.20.0'
    ]
)
