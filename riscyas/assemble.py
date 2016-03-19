"""
Placeholder.
"""
import click
import sys
from riscyas.instruction.utils.parse import AS_Parser


@click.command()
@click.argument('infile', type=click.File('r'))
@click.argument('outfile', type=click.File('wb'), nargs=-1)
@click.option('--text', is_flag=True, default=False)
def cli(infile, outfile, text):
    if not outfile:
        outfile = sys.stdout
    else:
        outfile = outfile[0]
    asssemble(infile, outfile, textmode=text)


def asssemble(instream, out_bytestream, textmode):
    for instruction in AS_Parser(instream):
        if textmode:
            out_bytestream.write(str([hex(c) for c in instruction]) + '\n')
        else:
            out_bytestream.write(instruction)
