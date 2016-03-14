import struct
import sys

class Endianess(object):
    """Object to represent the endianess of instructions. Wraps a endianess
    property with a setter.
    """
    __endianess_options = {'little': '<', 'big': '>'}
    endianess = None
    _instr_struct = None
    _instr_struct_format = 'xq'

    def __setattr__(self, name, value):
        if name == 'endianess':
            if self.endianess:
                raise Exception('endianess can only be set once!')
            elif value in Endianess.__endianess_options:
                self.__dict__[name] = value
                self._inst_struct = struct.Struct(
                        Endianess.__endianess_options[value] +
                        _instr_struct_format)

            else:
                # TODO: Modularize the suggestions.
                raise Exception("'%s' endianess doesn't exist. Try little or\
                        big." % value)
