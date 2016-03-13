import instbase
import sys, inspect

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

class ADD():
    pass
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
    return [obj for _ , obj in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(obj)]
