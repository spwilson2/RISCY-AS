
# import instructions
import re
from riscyas.instruction import instructions as risc_instrs

"""
This is a crude parser. It only makes a single pass.

TODO:
    At some point could have it preparse for directives etc.
"""


class AS_Parser(object):
    """
    Parser object which we can keep calling next on and it will return
    instuctions/commands.
    """
    print(risc_instrs.defined_instructions()[0].assembly_format)

    instruction_regex = {instr.__name__: re.compile(instr.assembly_format) for
                         instr in risc_instrs.defined_instructions()}


    def __init__(self, stream):
        # TODO: Likely at some point will need to move to a string object to
        # preparse rather than parse all in one shot.
        self._in_stream = stream

    def __iter__(self):
        # We might have multiple lines for a single command?
        # so allow it to go through multple lines.
        command_builder = ''

        for line in self._in_stream:

            command_builder += self.__strip(line)

            instruction = self.parse(command_builder)

            if instruction:
                command_builder = ''
                yield instruction

    def instruction_as_regex(instr):
        pass

    def parse(self, command):
        """Try parsing the command into an instruction. Return None if unable
        to.
        """
        if not command:
            return

        # Search through all instructions looking for this command. If not
        # found return None.
        instruction = command.split(' ')[0]
        try:
            return self.instruction_regex[instruction]
        except KeyError:
            return

    @staticmethod
    def __strip(line):
        """Strip the line on both sides of whitespace"""
        # TODO: Might be worthwile to make this clean the spaces in the middle
        # too ie: split(' ')
        return line.rstrip().lstrip()

if __name__ == '__main__':
    print(AS_Parser.instruction_regex)
