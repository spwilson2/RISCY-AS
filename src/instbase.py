""" Defines the instructions supported and their respective objects.
"""


class Instruction(object):
    """The ABC for assembly instructions."""
    def __init__(self):
        self.__operands = set()

class RInstuction(Instruction):
    """R-Type Instruction"""
    pass

class IInstuction(Instruction):
    """I-Type Instruction"""
    pass

class SInstuction(Instruction):
    """S-Type Instruction"""
    pass

class SBInstuction(Instruction):
    """SB-Type Instruction"""
    pass

class UInstuction(Instruction):
    """U-Type Instruction"""
    pass

class UJInstuction(Instruction):
    """UJ-Type Instruction"""
    pass

class SpecialInstruction(Instruction):
    """Non-Assembly Instruction"""
    pass

class Branch():#TODO
    pass

