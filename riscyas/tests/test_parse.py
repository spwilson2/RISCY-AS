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
