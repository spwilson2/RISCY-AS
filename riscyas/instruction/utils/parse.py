"""Defines the AS_Parser object which is used to parse a object that supports
iteration for strings which match Instructions and outputs their binary format.
"""

# import instructions
import re
from riscyas.instruction import instructions as risc_instrs

"""
This is a crude parser. It only makes a single pass.

TODO:
    At some point could have it pre-parse for directives etc.
"""

# TODO: For parsing out comments, just split on ';' and remove all except [0]


def make_operand_re(instruction_class):
    """Deprecated

    Takes the given instruction class and creates a regex that can be used
    to get operands.
    """
    re_string = instruction_class.__name__
    for operand in instruction_class.operand_tup._fields:
        re_string += '[ ]*(?P<%s>[^\s]*),' % operand

    # Get rid of the last comma of string.
    return re.compile(re_string[:-1])


class AS_Parser(object):
    """
    Parser object which we can keep calling next on and it will return
    instructions/commands.
    """
    instructions = {instr.__name__: {'class': instr, 'operand_re':
                                     instr.assembly_regex} for
                    instr in risc_instrs.defined_instructions()
                    }

    def __init__(self, stream):
        # TODO: Likely at some point will need to move to a string object to
        # pre-parse rather than parse all in one shot.
        self._in_stream = stream

    def __iter__(self):
        # We might have multiple lines for a single command?  So allow it to go
        # through multiple lines.
        command_builder = ''
        instruction = None

        for line in self._in_stream:

            # First get an instruction.
            if instruction is None:
                instruction = self._parse_instruction(line)

            # Try to instantiate an object from this instruction.
            if instruction is not None:

                # Get the operands for the instruction.
                command_builder += self.__strip(line)
                operands = self._parse_operands(command_builder, instruction)

                # Instantiate the instruction with the operands.
                if operands is not None:
                    yield instruction['class'](**operands).as_bytearray()

                    # Cleanup state to start processing the next instruction.
                    command_builder = ''
                    instruction = None

    def _parse_instruction(self, command):
        """Try parsing the command into an instruction. Return None if unable
        to.
        """
        if not command:
            return

        # Get the instruction name ex: ADD
        command = self.__strip(command)
        instruction = command.split(' ')[0]

        # Search through dict of all instructions looking for this command. If
        # not found return None.
        try:
            return self.instructions[instruction]
        except KeyError:
            return

    def _parse_operands(self, command, instruction):
        """Parse the command using the given instruction to look for operands.
        """

        if not command or not instruction:
            return

        match = instruction['operand_re'].search(command)

        if match:
            return {k: int(v) for k, v in match.groupdict().items()}

    @staticmethod
    def __strip(line):
        """Strip the line on both sides of whitespace"""
        return line.rstrip().lstrip()

if __name__ == '__main__':
    print(AS_Parser.instructions)
