import os
from setuptools import setup, find_packages
import warnings

setup(
    name='essh',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=6.6',
        'boto3>=1.2.2',
        'retrying>=1.3.3'
    ],
    entry_points={
        "console_scripts": [
            "essh=essh.cli:cli",
        ]
    },
    namespace_packages = ['essh'],
    author="Patrick Cullen",
    author_email="patrickbcullen@gmail.com",
    url="https://github.com/patrickbcullen/essh",
    download_url = "https://github.com/patrickbcullen/essh/tarball/v0.2.0",
    keywords = ['ssh', 'ec2', 'aws'],
    classifiers = []
)
