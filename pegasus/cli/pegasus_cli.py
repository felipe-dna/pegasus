import click

from pegasus.cli.logs import log


@click.group()
def main():
    pass


@main.command()
def init():
    log("Pegasus!", color="blue", figlet=True)
    log("Welcome to Pegasus, the asynchronous Python ORM!", "green")


@main.command()
@click.option('--file', '-F')
def migrate(file):
    pass


def cli():
    main()
