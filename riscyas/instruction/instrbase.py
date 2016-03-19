
""" Defines the instructions supported and their respective objects.  """

import bitstruct
import sys
import codecs
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


class Instruction(object):
    """The ABC for assembly instructions."""

    def __init__(self, *, opcode, byte_order=None):
        self._opcode = opcode
        self._byte_order = self._set_byte_order(byte_order)
        self._struct_frmt = None

    def __str__(self):
        """Instructions should be the same as their __name__"""
        return str(self.__class__)

    def as_bytearray(self):
        """Return the Instruction as an integer, needs to be implemented
        in subclasses.
        """
        raise Exception('as_bytearray Unimplemented in: %s' % self.__class__)

    def _set_byte_order(self, byte_order):
        if byte_order in ENDIAN_CHARMAP.keys():
            self._byte_order = byte_order
        else:
            self._byte_order = DEFAULT_BYTEORDER

    def pack(self, *args):
        packed = bitstruct.pack('>' + str(self._struct_frmt), *args)
        return packed if self._byte_order == 'big' else flip_bytes(packed)

    @classproperty
    def assembly_format(class_):
        return ' '.join((class_.__name__,
                         ', '.join(class_.operand_tup._fields)))


class RInstruction(Instruction):
    """R-Type Instruction"""
    super = Instruction

    r_operands = namedtuple('operands', ['rd', 'rs1', 'rs2'])
    operand_tup = r_operands

    def __init__(self, *, rd, rs1, rs2, opcode,
                 funct3, funct7, byte_order=None):

        RInstruction.super.__init__(self, byte_order=byte_order, opcode=opcode)
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

    def __init__(self, *, rd, rs1, imm, opcode, funct3):
        IInstruction.super.__init__(self, opcode)
        self._operands = IInstruction.i_operands(rd=rd, rs1=rs1, imm=imm)


class SInstruction(Instruction):
    """S-Type Instruction"""
    super = Instruction
    s_operands = IInstruction.i_operands

    def __init__(self, *, rd, rs1, imm, opcode, funct3):
        SInstruction.super.__init__(self, opcode)
        self._operands = SInstruction.s_operands(rd=rd, rs1=rs1, imm=imm)


class SBInstruction(Instruction):
    """SB-Type Instruction"""
    super = Instruction

    def __init__(self, *, rd, rs1, imm, opcode, funct3):
        SBInstruction.super.__init__(self, opcode)


class UInstruction(Instruction):
    """U-Type Instruction"""
    super = Instruction
    u_operands = namedtuple('operands', ['rd', 'imm'])

    def __init__(self, *, rd, imm, opcode):
        UInstruction.super.__init__(self, opcode)
        self._operands = UInstruction.u_operands(rd=rd, imm=imm)


class UJInstruction(UInstruction):
    """UJ-Type Instruction"""
    super = UInstruction

    def __init__(self, *, rd, imm, opcode):
        UJInstruction.super.__init__(self, rd, imm, opcode)


class SpecialInstruction():
    """Non-Assembly Instruction"""


class Branch():  # TODO
    pass

if __name__ == '__main__':
    r_type_instruction = RInstruction(funct7=1, rs2=1, rs1=1,
                                      funct3=1, rd=1, opcode=1)

    assert [hex(c) for c in r_type_instruction.as_bytearray()] ==\
            ['0x81', '0x90', '0x10', '0x2'] if sys.byteorder == 'little' else\
            ['0x2', '0x10', '0x90', '0x81'],\
            [hex(c) for c in r_type_instruction.as_bytearray()]

    print('------------- Self test successful -------------')
