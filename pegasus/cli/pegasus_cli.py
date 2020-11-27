import click

from pegasus.cli.logs import log


@click.group()
def main():
    pass


@main.command()
@click.argument('name')
def init(name: str):
    log("Pegasus CLI", color="blue", figlet=True)
    log("Welcome to Pegasus", "green")
    log(f"Creating {name} database...", "green")


def cli():
    main()
