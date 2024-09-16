"""Test cli"""

import click


@click.group()
def cli():
    """Test cli"""


@cli.command()
def hello():
    click.echo("Hello World!")


if __name__ == "__main__":
    cli()
