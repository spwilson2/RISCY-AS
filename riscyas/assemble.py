"""
Placeholder.
"""
import click
import sys
from riscyas.instruction.utils.parse import AS_Parser


@click.command()
@click.argument('infile', type=click.File('r'))
@click.argument('outfile', type=click.File('wb'), nargs=-1)
def cli(infile, outfile):
    if not outfile:
        outfile = sys.stdout
    asssemble(infile, outfile)


def asssemble(instream, out_bytestream):
    for instruction in AS_Parser(instream):
        out_bytestream.write(str(instruction) + '\n')
