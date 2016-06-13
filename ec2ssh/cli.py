#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
@click.argument('target')
def cli(target):
	print target

if __name__ == '__main__':
    cli()
