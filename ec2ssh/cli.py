#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from ec2.controller import EC2Controller
from ssh.controller import SSHController

@click.command()
@click.argument('target')
def cli(target):
    ec2_controller = EC2Controller()
    instance = ec2_controller.find(target)
    SSHController(instance.keypair, instance.private_ip).ssh()

if __name__ == '__main__':
    cli()
