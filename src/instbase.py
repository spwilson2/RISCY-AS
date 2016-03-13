
""" Defines the instructions supported and their respective objects.  """

from collections import namedtuple


r_operands = namedtuple('r_operands', ['rd', 'rs1', 'rs2'])
i_operands = namedtuple('r_operands', ['rd', 'rs1', 'imm'])


class Instruction(object):
    """The ABC for assembly instructions."""
    def __init__(self):
        pass

    def __str__(self):
        """Instructions should be the same as their __name__"""
        return str(self.__name__)


class RInstruction(Instruction):
    """R-Type Instruction"""
    def __init__(self, rd, rs1, rs2):
        self._operands = r_operands(rd=rd, rs1=rs1, rs2=rs2)


class IInstruction(Instruction):
    """I-Type Instruction"""
    def __init__(self, rd, rs1, imm):
        self._operands = r_operands(rd=rd, rs1=rs1, imm=imm)


class SInstruction(Instruction):
    """S-Type Instruction"""
    pass


class SBInstruction(Instruction):
    """SB-Type Instruction"""
    pass


class UInstruction(Instruction):
    """U-Type Instruction"""
    pass


class UJInstruction(Instruction):
    """UJ-Type Instruction"""
    pass


class SpecialInstruction(Instruction):
    """Non-Assembly Instruction"""
    pass


class Branch():  # TODO
    pass
