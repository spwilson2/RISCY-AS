import sys
import inspect
from riscyas.instruction.instrbase import RInstruction, UInstruction

"""
TODO:
    Make a class generator for these.
"""


class LUI(UInstruction):
    super = UInstruction

    __opcode = 0b0110111

    def __init__(self, imm, rd):
        self.super.__init__(self, imm=imm,
                            rd=rd, opcode=self.__opcode)


class JAL(UInstruction):
    super = UInstruction
    __opcode = 0b1101111

    def __init__(self, imm, rd):
        self.super.__init__(self, imm=imm,
                            rd=rd, opcode=self.__opcode)


#class BEQ():
#    pass
#class BNE():
#    pass
#class BLT():
#    pass
#class BGE():
#    pass
#class BLTU():
#    pass
#class BGEU():
#    pass
#class LW():
#    pass
#class SW():
#    pass
#class ADDI():
#    pass
#class XORI():
#    pass
#class ORI():
#    pass
#class ANDI():
#    pass


class ADD(RInstruction):
    super = RInstruction
    __opcode = 0b0110011
    __funct3 = 0b000
    __funct7 = 0b0000000

    def __init__(self, rs1, rs2, rd):

        self.super.__init__(self, rs1=rs1, rs2=rs2, rd=rd,
                           funct3=self.__funct3,
                           funct7=self.__funct7,
                           opcode=self.__opcode
                           )


class SUB(RInstruction):
    super = RInstruction
    __opcode = 0b0110011
    __funct3 = 0b000
    __funct7 = 0b0100000

    def __init__(self, rs1, rs2, rd):

        self.super.__init__(self, rs1=rs1, rs2=rs2, rd=rd,
                           funct3=self.__funct3,
                           funct7=self.__funct7,
                           opcode=self.__opcode
                           )


class XOR(RInstruction):
    super = RInstruction
    __opcode = 0b0110011
    __funct3 = 0b100
    __funct7 = 0b0000000

    def __init__(self, rs1, rs2, rd):

        self.super.__init__(self, rs1=rs1, rs2=rs2, rd=rd,
                           funct3=self.__funct3,
                           funct7=self.__funct7,
                           opcode=self.__opcode
                           )


class OR(RInstruction):
    super = RInstruction
    __opcode = 0b0110011
    __funct3 = 0b110
    __funct7 = 0b0000000

    def __init__(self, rs1, rs2, rd):

        self.super.__init__(self, rs1=rs1, rs2=rs2, rd=rd,
                           funct3=self.__funct3,
                           funct7=self.__funct7,
                           opcode=self.__opcode
                           )


class AND(RInstruction):
    super = RInstruction
    __opcode = 0b0110011
    __funct3 = 0b111
    __funct7 = 0b0000000

    def __init__(self, rs1, rs2, rd):

        self.super.__init__(self, rs1=rs1, rs2=rs2, rd=rd,
                           funct3=self.__funct3,
                           funct7=self.__funct7,
                           opcode=self.__opcode
                           )


#class SBREAK():
#    pass
#class NOP():
#    pass


def defined_instructions():
    """Return a list of the instructions defined in this file."""
    # FIXME: There probably is a better way to do this with inheritence
    # detection.
    #return [ADD]

    #return [ADD]
    return [obj for _, obj in inspect.getmembers(sys.modules[__name__]) if
        inspect.isclass(obj)]
    #        if inspect.isclass(obj)]

if __name__ == '__main__':
    print('Starting self test.')
    # TODO: Add assertion for correct val on as_bytearray
    for _ in range(50000):
        add_instr = ADD(rs1=1, rs2=1, rd=1)
        add_instr.as_bytearray()
    print(add_instr.as_bytearray())
