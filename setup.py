import os
from setuptools import setup, find_packages
import warnings

setup(
    name='ec2ssh',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click>=6.6',
    ],
    entry_points={
        "console_scripts": [
            "ec2ssh=ec2ssh.cli:cli",
        ]
    },
    namespace_packages = ['ec2ssh'],
    author="Patrick Cullen",
    url="https://github.com/patrickbcullen/ec2ssh",
    download_url = "https://github.com/patrickbcullen/ec2ssh/tarball/v0.1.0",
    keywords = ['ssh', 'ec2', 'aws'],
    classifiers = []
)
