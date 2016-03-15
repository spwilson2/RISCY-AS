import sys
import inspect
import riscyas.instruction.instrbase

"""
TODO:
    Use __name__ to check for the instruction when parsing.
"""

class LUI():
    pass
class JAL():
    pass

class BEQ():
    pass
class BNE():
    pass
class BLT():
    pass
class BGE():
    pass
class BLTU():
    pass
class BGEU():
    pass
class LW():
    pass
class SW():
    pass
class ADDI():
    pass
class XORI():
    pass
class ORI():
    pass
class ANDI():
    pass


class ADD(instrbase.RInstruction):
    super = instrbase.RInstruction
    __opcode = 0b0110011
    __funct3 = 0b111
    __funct7 = 0b0000000

    def __init__(self, rs1, rs2, rd):

        ADD.super.__init__(self, rs1=rs1, rs2=rs2, rd=rd,
                           funct3=ADD.__funct3,
                           funct7=ADD.__funct7,
                           opcode=ADD.__opcode
                           )

class SUB():
    pass
class XOR():
    pass
class OR():
    pass
class AND():
    pass
class SBREAK():
    pass
class NOP():
    pass


def defined_instructions():
    """Return a list of the instructions defined in this file."""
    # FIXME: There probably is a better way to do this with inheritence
    # detection.
    return [obj for _, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj)]

if __name__ == '__main__':
    print('Starting self test.')
    # TODO: Add assertion for correct val on as_bytearray
    for _ in range(50000):
        add_instr = ADD(rs1=1, rs2=1, rd=1)
        add_instr.as_bytearray()
    print(add_instr.as_bytearray())
