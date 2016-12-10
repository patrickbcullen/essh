#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from ec2.controller import EC2Controller
from ssh.controller import SSHController

@click.command()
@click.option('--keypair-dir', default="~/.ssh", help='Directory where keypair files are located')
@click.option('--keypair-extension', default="pem", help='File extension for keypari files')
@click.argument('target')
@click.argument('command', nargs=-1)
def cli(keypair_dir, keypair_extension, target, command):
    cmd = " ". join(command)
    if len(cmd) > 0:
        cmd = " " + cmd

    ec2_controller = EC2Controller()
    instance = ec2_controller.find(target)
    SSHController(keypair_dir, instance.keypair, keypair_extension, instance.private_ip).ssh(cmd)

if __name__ == '__main__':
    cli()
