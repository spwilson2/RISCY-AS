from io import StringIO
from textwrap import dedent
import unittest
from unittest import TestCase

import riscyas.instruction.utils.parse
from riscyas.instruction.utils.parse import AS_Parser, ADD

class TestParse(TestCase):
    def test_import(self):
        pass

    def test_instantiate(self):
        obj = AS_Parser(StringIO())
        self.assertIsInstance(obj, AS_Parser)

    def test_parse_instruction(self):
        obj = AS_Parser(StringIO())
        self.assertIs(obj._parse_instruction('ADD 1,2,3')['class'], ADD)

    #def test_make_operand_re(self):
    #    from riscyas.instruction.instructions import ADD
    #    from riscyas.instruction.utils.parse import make_operand_re
    #    print(make_operand_re(ADD))

    def test_parse_operands(self):
        obj = AS_Parser(StringIO('ADD 1,2,3'))

        instruction = obj._parse_instruction('ADD 1,2,3')
        print(instruction)

        try:
            parsed_operands = obj._parse_operands('ADD 1,2,3', instruction)
        except Exception as e:
            print(e)

        self.assertEqual(parsed_operands, {'rd':1,'rs1':2,'rs2':3})

    def test_single_parse(self):
        obj = AS_Parser(StringIO('ADD 1,2,2'))
        try:
            parsed = next(iter(obj))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise
        print(parsed)

    def test_multiple_parse(self):

        instr_stream = """\
        ADD 1,2,3
        ADD 2,3,4
        ADD 3,4,5"""
        instr_stream = dedent(instr_stream)

        obj = AS_Parser(StringIO(instr_stream))
        try:
            for line in instr_stream.splitlines():
                print(line)
                parsed = next(iter(obj))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise

    def test_multiline(self):

        instr_stream = """\
        ADD 1,2,3

        ADD 3,4,5"""
        instr_stream = dedent(instr_stream)

        obj = AS_Parser(StringIO(instr_stream))
        try:
            for _ in range(2):
                parsed = next(iter(obj))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise

    def test_multiline2(self):

        instr_stream = """\
        ADD
        1,2,3

        ADD 3,4,5"""
        instr_stream = dedent(instr_stream)

        obj = AS_Parser(StringIO(instr_stream))
        try:
            for _ in range(2):
                parsed = next(iter(obj))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise

    def test_UInstruction(self):

        obj = AS_Parser(StringIO('LUI 1,100'))
        try:
            parsed = next(iter(obj))
            self.assertEqual(parsed, bytearray(b'\xb7\x40\x06\x00'))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise

    def test_UInstruction(self):

        obj = AS_Parser(StringIO('ADDI 1,2,100'))
        try:
            parsed = next(iter(obj))
            # TODO: Add expected val.
            # self.assertEqual(parsed, bytearray(b''))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise

    def test_SBInstruction(self):

        obj = AS_Parser(StringIO('BEQ 1,2,100'))
        try:
            parsed = next(iter(obj))
            # TODO: Add expected val.
            #self.assertEqual(parsed, bytearray(b''))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise

    def test_SInstruction(self):

        obj = AS_Parser(StringIO('SW 1,2,100'))
        try:
            parsed = next(iter(obj))
            # TODO: Add expected val.
            # self.assertEqual(parsed, bytearray(b''))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise

    def test_OInstruction(self):

        obj = AS_Parser(StringIO('NOP'))
        try:
            parsed = next(iter(obj))
            # TODO: Add expected val.
            self.assertEqual(parsed, bytearray(b'\x33\x00\x00\x00'))
        except StopIteration:
            print('Couldn\'t match a instruction.')
            raise

