
""" Defines the instructions supported and their respective objects.  """

import bitstruct
import sys
import codecs
import re
from collections import namedtuple

# TODO: The maker of bitstruct used bitorder instead of byte order...
# Add a wrapper to it's output -,-

DEFAULT_BYTEORDER = sys.byteorder

ENDIAN_CHARMAP = {'little': '<', 'big': '>'}


class ClassPropertyDescriptor(object):

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError("can't set attribute")
        type_ = type(obj)
        return self.fset.__get__(obj, type_)(value)

    def setter(self, func):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self


def classproperty(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)

    return ClassPropertyDescriptor(func)


# TODO: This functions is so wtf. Find out a better way to flip byte order.
def flip_bytes(byte_array):
    hex_array = [hex(byte) for byte in byte_array]
    hex_array.reverse()
    flippedstring = hex_array
    flippedstring = [hex_string[2:] for hex_string in flippedstring]
    for idx, hex_val in enumerate(flippedstring):
        if len(hex_val) == 1:
            flippedstring[idx] = '0' + hex_val

    flippedstring = ''.join(flippedstring)
    return bytearray(codecs.decode(flippedstring, 'hex'))


def get_bitslice(obj, topidx, bottomidx):
    """Returns the bits within obj[bottomidx:topidx+1] (Or in architecture format
    obj[topidx:bottomidx])
    """
    obj = obj >> bottomidx

    # Generate a bitmask to get topidx - bottomidx number bits
    mask = 1
    for bit in range(topidx - bottomidx):
        mask = mask << 1
        mask += 1
    return obj & mask


class Instruction(object):
    """The Base Class for all assembly instructions."""

    def __init__(self, *, opcode, byteorder=None):
        self._opcode = opcode
        self._byteorder = self._set_byteorder(byteorder)
        self._struct_frmt = None

    def __str__(self):
        """Instructions should be the same as their __name__"""
        return str(self.__class__)

    def as_bytearray(self):
        """Return the Instruction as an integer, needs to be implemented in
        subclasses.
        """
        raise UnimplementedException('as_bytearray Unimplemented in: %s' %
                                     self.__class__)

    def _set_byteorder(self, byteorder):
        if byteorder in ENDIAN_CHARMAP.keys():
            self._byteorder = byteorder
        else:
            self._byteorder = DEFAULT_BYTEORDER

    def pack(self, *args):
        """Pack the given arguements into a bytearray using the format
        specified in `self._struct_frmt`. This is done at the bit level, rather
        than the normal python byte packing level.
        """
        packed = bitstruct.pack('>' + str(self._struct_frmt), *args)
        return packed if self._byteorder == 'big' else flip_bytes(packed)

    @classproperty
    def assembly_format(class_):
        """Return the format of the instruction in assembly"""
        return ' '.join((class_.__name__,
                         ', '.join(class_.operand_tup._fields)))

    @classproperty
    def assembly_regex(class_):
        """Return a regex that can be used to search for all values within
        `class_.operand_tup`.
        """
        re_string = class_.__name__
        for operand in class_.operand_tup._fields:
            re_string += '[ ]*[%%$]?(?P<%s>[\d]*),' % operand
        return re.compile(re_string[:-1])


class RInstruction(Instruction):
    """R-Type Instruction"""
    super = Instruction

    r_operands = namedtuple('operands', ['rd', 'rs1', 'rs2'])
    operand_tup = r_operands

    def __init__(self, *, rd, rs1, rs2, opcode,
                 funct3, funct7, byteorder=None):

        RInstruction.super.__init__(self, byteorder=byteorder, opcode=opcode)
        self._operands = RInstruction.r_operands(rd=rd, rs1=rs1, rs2=rs2)
        self._funct3 = funct3
        self._funct7 = funct7
        self._struct_frmt = 'u7u5u5u3u5u7'

    def as_bytearray(self):
        return self.pack(
                self._funct7, self._operands.rs2,
                self._operands.rs1, self._funct3,
                self._operands.rd, self._opcode
                )


class IInstruction(Instruction):
    """I-Type Instruction"""
    super = Instruction
    i_operands = namedtuple('operands', ['rd', 'rs1', 'imm'])
    operand_tup = i_operands

    def __init__(self, *, rd, rs1, imm, opcode, funct3, byteorder=None):
        IInstruction.super.__init__(self, opcode=opcode, byteorder=byteorder)
        self._operands = IInstruction.i_operands(rd=rd, rs1=rs1, imm=imm)
        self._funct3 = funct3
        self._struct_frmt = 'u12u5u3u5u7'

    def as_bytearray(self):
        return self.pack(
                self._operands._imm, self._operands.rs1,
                self._funct3, self._operands.rd,
                self._opcode
                )

#################################################
######## TODO: Look at init and as_bytearray ########
#################################################


class SInstruction(Instruction):
    """S-Type Instruction"""
    super = Instruction
    s_operands = namedtuple('operands', ['rs1', 'rs2', 'imm'])
    operand_tup = s_operands

    def __init__(self, *, byteorder=None, rs1, rs2, imm, opcode, funct3):
        SInstruction.super.__init__(self, opcode, byteorder=None)
        self._operands = SInstruction.s_operands(rs1=rs1, rs2=rs2, imm=imm)
        self._funct3 = funct3
        self._struct_frmt = 'u7u5u5u3u7'

    def as_bytearray(self):
        return self.pack(
                get_bitslice(self._operands._imm, 11, 5),
                self._operands.rs2, self._operands.rs1,
                self._funct3,
                get_bitslice(self._operands._imm, 4, 0),
                self._opcode
                )


class SBInstruction(SInstruction):
    """SB-Type Instruction"""
    super = SInstruction

    def __init__(self, *, byteorder=None, rd, rs1, imm, opcode, funct3):
        SBInstruction.super.__init__(self, rd=rd, rs1=rs1, imm=imm,
                                     opcode=opcode, funct3=funct3,
                                     byteorder=byteorder)
        self._struct_frmt = 'u1u6u5u5u3u4u1u7'

    def as_bytearray(self):
        return self.pack(
                get_bitslice(self._operands._imm, 12, 12),
                get_bitslice(self._operands._imm, 10, 5),
                self._operands.rs2, self._operands.rs1,
                self._funct3,
                get_bitslice(self._operands._imm, 4, 1),
                get_bitslice(self._operands._imm, 11, 11),
                self._opcode
                )


class UInstruction(Instruction):
    """U-Type Instruction"""
    super = Instruction
    u_operands = namedtuple('operands', ['rd', 'imm'])
    operand_tup = u_operands

    def __init__(self, *, byteorder=None, rd, imm, opcode):
        UInstruction.super.__init__(self, opcode=opcode, byteorder=byteorder)
        self._operands = UInstruction.u_operands(rd=rd, imm=imm)
        self._struct_frmt = 'u20u5u7'

    def as_bytearray(self):
        # TODO: I don't remember how the risc spec works for this imm[31:12]
        # will need to look that up for this imm.
        return self.pack(
                self._operands.imm,
                self._operands.rd, self._opcode
                )


class UJInstruction(UInstruction):
    """UJ-Type Instruction"""
    super = UInstruction

    def __init__(self, *, rd, imm, opcode, byteorder=None):
        UJInstruction.super.__init__(self, rd=rd, imm=imm, opcode=opcode,
                byteorder=byteorder)


class SpecialInstruction():
    """Non-Assembly Instruction"""


class Branch():  # TODO
    pass


class UnimplementedException(Exception):
    pass

if __name__ == '__main__':
    r_type_instruction = RInstruction(funct7=1, rs2=1, rs1=1,
                                      funct3=1, rd=1, opcode=1)

    assert [hex(c) for c in r_type_instruction.as_bytearray()] ==\
            ['0x81', '0x90', '0x10', '0x2'] if sys.byteorder == 'little' else\
            ['0x2', '0x10', '0x90', '0x81'],\
            [hex(c) for c in r_type_instruction.as_bytearray()]

    print('------------- Self test successful -------------')
