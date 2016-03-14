
""" Defines the instructions supported and their respective objects.  """

import struct
import sys
import endianess
from collections import namedtuple


class Instruction(object):
    """The ABC for assembly instructions."""
    def __init__(self, opcode):
        self._opcode = opcode

    def __str__(self):
        """Instructions should be the same as their __name__"""
        return str(self.__name__)

    def as_int(self):
        """Return the Instruction as an integer, needs to be implemented
        in subclasses.
        """
        raise Exception('as_int Unimplemented in: %s' % self.__name__)


class RInstruction(Instruction):
    """R-Type Instruction"""
    super = Instruction

    def __init__(self, rd, rs1, rs2, opcode, funct3, funct7):
        super.__init__(self, opcode)
        self._operands = r_operands(rd=rd, rs1=rs1, rs2=rs2)
        self._funct3 = funct3
        self._funct7 = funct7

    def as_int(self):
        return _inst_struct.pack(self._funct7, self._operands.rs2,
                                 self._operands.rs1, self._funct3,
                                 self._operands.rd, self._opcode)


class IInstruction(Instruction):
    """I-Type Instruction"""
    super = Instruction

    def __init__(self, rd, rs1, imm, opcode, funct3):
        super.__init__(self, opcode)
        self._operands = i_operands(rd=rd, rs1=rs1, imm=imm)


class SInstruction(Instruction):
    """S-Type Instruction"""
    super = Instruction

    def __init__(self, rd, rs1, imm, opcode, funct3):
        super.__init__(self, opcode)
        self._operands = s_operands(rd=rd, rs1=rs1, imm=imm)


class SBInstruction(Instruction):
    """SB-Type Instruction"""
    super = Instruction

    def __init__(self, rd, rs1, imm, opcode, funct3):
        super.__init__(self, opcode)
        self._operands = s_operands(rd=rd, rs1=rs1, imm=imm)


class UInstruction(Instruction):
    """U-Type Instruction"""
    super = Instruction

    def __init__(self, rd, imm, opcode):
        super.__init__(self, opcode)
        self._operands = s_operands(rd=rd, imm=imm)


class UJInstruction(UInstruction):
    """UJ-Type Instruction"""
    super = UInstruction

    def __init__(self, rd, imm, opcode):
        super.__init__(self, rd, imm, opcode)


class SpecialInstruction():
    """Non-Assembly Instruction"""


class Branch():  # TODO
    pass

r_operands = namedtuple('operands', ['rd', 'rs1', 'rs2'])
i_operands = namedtuple('operands', ['rd', 'rs1', 'imm'])
s_operands = i_operands
u_operands = namedtuple('operands', ['rd', 'imm'])
