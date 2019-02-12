from unittest import TestCase


class TestProd(TestCase):
    def test_prod(self):
        from prod_1004 import prod

        result = prod(9, 3)

        self.assertEqual(27, result)
