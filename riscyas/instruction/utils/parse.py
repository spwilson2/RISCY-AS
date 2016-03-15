
# import instructions

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

    def __init__(self, stream):
        # TODO: Likely at some point will need to move to a string object to
        # preparse rather than parse all in one shot.
        self._in_stream = stream

    def __itr__(self):
        # We might have multiple lines for a single command?
        # so allow it to go through multple lines.
        command_builder = ''

        for line in self._in_stream:

            command_builder += self.__strip(line)

            instruction = self.parse(command_builder)

            if instruction:
                yield instruction

    def parse(self, command):
        """Try parsing the command into an instruction. Return None if unable
        to.
        """

        if not command:
            return

    @staticmethod
    def __strip(line):
        """Strip the line on both sides of whitespace"""
        # TODO: Might be worthwile to make this clean the spaces in the middle
        # too ie: split(' ')
        return line.rstrip().lstrip()
