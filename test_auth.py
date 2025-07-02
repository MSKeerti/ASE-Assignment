import unittest
from app import is_prime

class TestIsPrime(unittest.TestCase):
    def test_positive_case(self):
        self.assertTrue(is_prime(5))  # should pass

    def test_negative_case(self):
        self.assertFalse(is_prime(4))  # should also pass now

    def test_intentional_fail(self):
        self.assertTrue(False, "Intentional failure to test Jenkins alerting")
