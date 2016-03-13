"""
Placeholder.
"""
import click

@click.command()
@click.argument('infile', type=click.File('r'))
@click.argument('outfile', type=click.File('wb'), nargs=-1)
def cli(infile, outfile):
    pass
