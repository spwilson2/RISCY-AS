from unittest import TestCase

class TestInstrbase(TestCase):
    def test_import(self):
        import riscyas.instruction.instrbase

    def test_get_bitslice(self):
        from riscyas.instruction.instrbase import get_bitslice

        self.assertEqual(get_bitslice(3, 1, 1), 1)
        self.assertEqual(get_bitslice(16, 4, 4), 1)
        self.assertEqual(get_bitslice(14, 3, 1), 7)

