import unittest
from unittest import TestCase

class TestParse(TestCase):
    def test_import(self):
        import riscyas.instruction.utils.parse

    def test_instantiate(self):
        from riscyas.instruction.utils.parse import AS_Parser
        from io import StringIO
        obj = AS_Parser(StringIO())
        self.assertIsInstance(obj, AS_Parser)

    def test_parse_instruction(self):
        from riscyas.instruction.utils.parse import AS_Parser
        from riscyas.instruction.instructions import ADD
        from io import StringIO
        obj = AS_Parser(StringIO())
        self.assertIs(obj._parse_instruction('ADD 1,2,3')['class'], ADD)

    def test_parse_operands(self):
        from riscyas.instruction.utils.parse import AS_Parser
        from io import StringIO
        obj = AS_Parser(StringIO('ADD 1,2,3'))

        instruction = obj._parse_instruction('ADD 1,2,3')
        print(instruction)

        try:
            parsed_operands = obj._parse_operands('ADD 1,2,3', instruction)
        except Exception as e:
            print(e)

        self.assertEqual(parsed_operands, {'rd':'1','rs1':'2','rs2':'3'})

    def test_single_parse(self):
        from riscyas.instruction.utils.parse import AS_Parser
        from io import StringIO
        obj = AS_Parser(StringIO('ADD 1,2,2'))
        try:
            parsed = next(iter(obj))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise
        print(parsed)

    def test_make_operand_re(self):
        from riscyas.instruction.instructions import ADD
        from riscyas.instruction.utils.parse import make_operand_re
        print(make_operand_re(ADD))
