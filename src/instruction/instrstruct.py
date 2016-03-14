
"""Provides the struct used to store instructions within binary files."""

from __future__ import print_function
import struct
import sys


class Struct(struct.Struct):
    """Conveniece wrapper around struct.Struct class to only need to apply
    the byteorder.
    """

    def __init__(self, byteorder):
        self._byteorder = None
        self._init_byteorder(byteorder)
        struct.Struct.__init__(self, self.frmt)

    def _init_byteorder(self, byteorder):
        """Initialize the byte order."""

        self._byteorder = check_byteorder(byteorder)

    @property
    def frmt(self):
        """Property defining the format of the struct using frmt strings from
        the struct pkg."""

        _frmt = 'xL'
        return ENDIAN_CHARMAP[self._byteorder] + _frmt

    @frmt.setter
    def set(self):
        """Disable setting for frmt."""

        raise Exception("Can't set frmt.")


class BadByteorderException(Exception):
    pass

ENDIAN_CHARMAP = {'little': '<',
                  'big': '>',
                  None: '@'}

DEFAULT_BYTEORDER = sys.byteorder


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

# Self test
# TODO: Make their ouput clear. (Ouptut the left side too.)
if __name__ == '__main__':
    try:
        Struct(byteorder='hello')
    except BadByteorderException:
        pass
    else:
        assert False, 'Expected to fail with a BadByteorderException'

    test_struct = Struct(byteorder='little')
    assert test_struct._byteorder == 'little', test_struct._byteorder

    test_struct = Struct(byteorder='big')
    assert test_struct._byteorder == 'big', test_struct._byteorder

    # Test that when we put in None as byteorder we create a default
    # byteorder Struct and that a warning is output to stderr.
    from StringIO import StringIO
    stderr = sys.stderr
    stderr_redir = sys.stderr = StringIO()

    test_struct = Struct(None)

    sys.stderr = stderr

    assert test_struct._byteorder is None, test_struct._byteorder
    assert test_struct.frmt == '@xL'
    assert stderr_redir.getvalue().rstrip() == \
        "WARN: byteorder not given, using system byteorder.",\
        stderr_redir.getvalue().rstrip()

    print('---------- PASSED SELF TEST -----------')
