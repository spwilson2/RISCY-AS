import sys
import inspect
from riscyas.instruction.instrbase import RInstruction, UInstruction,\
IInstruction, SBInstruction

"""
TODO:
    * Make a class generator for these.
    * improve the export of these.
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

class BEQ(SBInstruction):
    super = SBInstruction
    __opcode = 0b1100011
    __funct3 = 0b000

    def __init__(self, rs1, rs2, imm):

        self.super.__init__(self, rs1=rs1, rs2=rs2, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )


class BNE(SBInstruction):
    super = SBInstruction
    __opcode = 0b1100011
    __funct3 = 0b001

    def __init__(self, rs1, rs2, imm):

        self.super.__init__(self, rs1=rs1, rs2=rs2, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )


class BLT(SBInstruction):
    super = SBInstruction
    __opcode = 0b1100011
    __funct3 = 0b100

    def __init__(self, rs1, rs2, imm):

        self.super.__init__(self, rs1=rs1, rs2=rs2, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )


class BGE(SBInstruction):
    super = SBInstruction
    __opcode = 0b1100011
    __funct3 = 0b101

    def __init__(self, rs1, rs2, imm):

        self.super.__init__(self, rs1=rs1, rs2=rs2, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )



class BLTU(SBInstruction):
    super = SBInstruction
    __opcode = 0b1100011
    __funct3 = 0b110

    def __init__(self, rs1, rs2, imm):

        self.super.__init__(self, rs1=rs1, rs2=rs2, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )


class BGEU(SBInstruction):
    super = SBInstruction
    __opcode = 0b1100011
    __funct3 = 0b111

    def __init__(self, rs1, rs2, imm):

        self.super.__init__(self, rs1=rs1, rs2=rs2, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )

#class SW():
#    pass

class LW(IInstruction):
    super = IInstruction
    __opcode = 0b0000011
    __funct3 = 0b010

    def __init__(self, rs1, rd, imm):

        self.super.__init__(self, rs1=rs1, rd=rd, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )


class ADDI(IInstruction):
    super = IInstruction
    __opcode = 0b0010011
    __funct3 = 0b000

    def __init__(self, rs1, rd, imm):

        self.super.__init__(self, rs1=rs1, rd=rd, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )


class XORI(IInstruction):
    super = IInstruction
    __opcode = 0b0010011
    __funct3 = 0b100

    def __init__(self, rs1, rd, imm):

        self.super.__init__(self, rs1=rs1, rd=rd, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )


class ORI(IInstruction):
    super = IInstruction
    __opcode = 0b0010011
    __funct3 = 0b110

    def __init__(self, rs1, rd, imm):

        self.super.__init__(self, rs1=rs1, rd=rd, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )


class ANDI(IInstruction):
    super = IInstruction
    __opcode = 0b0010011
    __funct3 = 0b111

    def __init__(self, rs1, rd, imm):

        self.super.__init__(self, rs1=rs1, rd=rd, imm=imm,
                           funct3=self.__funct3,
                           opcode=self.__opcode
                           )


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
