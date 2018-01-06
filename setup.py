"""Package setup for dogfactory."""
from setuptools import setup

setup(
    name='dogfactory',  # required
    packages=['dogfactory'],  # required
    entry_points={
        'console_scripts': ['makedog=dogfactory.makedog:main']
    },
    version='1.0',  # required
    description='A factory that makes dogs! (The best kind of factory.)',
    author='Chelsea Dole',
    author_email='chelseadole@gmail.com',
    url='https://github.com/chelseadole/dogfactory',
    keywords=['dogs', 'factory', 'woof']
)
