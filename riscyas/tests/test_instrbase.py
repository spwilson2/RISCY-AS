from unittest import TestCase
from riscyas.instruction.instrbase import get_bitslice

class TestInstrbase(TestCase):
    def test_import(self):
        pass

    def test_get_bitslice(self):

        self.assertEqual(get_bitslice(3, 1, 1), 1)
        self.assertEqual(get_bitslice(16, 4, 4), 1)
        self.assertEqual(get_bitslice(14, 3, 1), 7)

