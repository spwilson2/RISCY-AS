from unittest import TestCase

class TestAs(TestCase):
    def can_import(self):
        import riscyas.assemble as riscas
        self.assertTrue(True)
