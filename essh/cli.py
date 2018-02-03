#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from ec2.controller import EC2Controller
from ssh.controller import SSHController
from essh.exceptions import ESSHException

@click.command(context_settings=dict(ignore_unknown_options=True,))
@click.option('--profile', '-p', help='AWS credentials profile (i.e. ~/.aws/credentials)')
@click.option('--zone', '-z', help='Filter hosts by availability zone specified (i.e. us-east-1a)')
@click.option('--keypair-dir', default="~/.ssh", help='Directory where keypair files are located')
@click.option('--keypair-extension', default="pem", help='File extension for keypari files')
@click.argument('target')
@click.argument('command', nargs=-1, type=click.UNPROCESSED)
def cli(profile, zone, keypair_dir, keypair_extension, target, command):
    cmd = " ". join(command)
    if len(cmd) > 0:
        cmd = " " + cmd

    ec2_controller = EC2Controller(profile, zone)
    try:
        instance = ec2_controller.find(target)
        SSHController(keypair_dir, instance.keypair, keypair_extension, instance.private_ip).ssh(cmd)
    except ESSHException as ex:
        print(ex.message)

if __name__ == '__main__':
    cli()
