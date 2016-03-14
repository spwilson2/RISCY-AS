
"""Provides the struct used to store instructions within binary files."""
# TODO: Add automatic detection and creation of format string based on
# int.bitlength

from __future__ import print_function
import click
import bitstruct
import sys


class Struct(object):
    """Conveniece wrapper around struct.Struct class to only need to apply
    the byteorder.
    """

    def __init__(self, byteorder, frmt):
        self._byteorder = None
        self._frmt = frmt
        self._init_byteorder(byteorder)

    def _init_byteorder(self, byteorder):
        """Initialize the byte order."""

        self._byteorder = check_byteorder(byteorder)

    @property
    def frmt(self):
        """Property defining the format of the struct using frmt strings from
        the struct pkg."""

        return ENDIAN_CHARMAP[self._byteorder] + self._frmt

    @frmt.setter
    def set(self):
        """Disable setting for frmt outside of init."""

        raise Exception("Can't set frmt.")

    def pack(self, *args):
        """Pack the arguments into a bytearray"""
        return bitstruct.pack(self.frmt, *args)


class BadByteorderException(Exception):
    pass


ENDIAN_CHARMAP = {'little': '<',
                  'big': '>'
                  }

DEFAULT_BYTEORDER = sys.byteorder
ENDIAN_CHARMAP[None] = ENDIAN_CHARMAP[DEFAULT_BYTEORDER]


def check_byteorder(byteorder):
    """Return whether the byteorder string is valid or not."""

    if not byteorder:
        print('WARN: byteorder not given, using system byteorder.',
              file=sys.stderr)
        return None

    elif byteorder in ENDIAN_CHARMAP.keys():
        return byteorder

    else:
        raise BadByteorderException('%s not a valid byteorder.\
                                    Try little or big.' % byteorder)


# TODO: Make this into a group that can just run all or a single self test.
@click.command()
def test_instrstruct():
    try:
        Struct(byteorder='hello', frmt='u1u2u3')
    except BadByteorderException:
        pass
    else:
        assert False, 'Expected to fail with a BadByteorderException'

    test_struct = Struct(byteorder='little', frmt='u1u2u3')
    assert test_struct._byteorder == 'little', test_struct._byteorder

    test_struct = Struct(byteorder='big', frmt='u1u2u3')
    assert test_struct._byteorder == 'big', test_struct._byteorder

    # Test that when we put in None as byteorder we create a default
    # byteorder Struct and that a warning is output to stderr.
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO

    stderr = sys.stderr
    stderr_redir = sys.stderr = StringIO()

    test_struct = Struct(None, frmt='u1u2u3')

    sys.stderr = stderr

    assert test_struct._byteorder is None, test_struct._byteorder
    assert test_struct.frmt == '<u1u2u3', test_struct.frmt
    assert stderr_redir.getvalue().rstrip() == \
        "WARN: byteorder not given, using system byteorder.",\
        stderr_redir.getvalue().rstrip()

    # Try packing some args.
    test_struct = Struct('big', frmt='u1u3u4')
    assert test_struct.pack(0,1,3) == b'\x13', test_struct.pack(0, 1, 3)

    print('---------- PASSED SELF TEST -----------')

# Self test
if __name__ == '__main__':
    test_instrstruct
