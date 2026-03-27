import unittest
from django.test import TestCase


class SimpleHealthCheckTest(TestCase):
    """Basic tests to verify Django is running"""

    def test_django_setup(self):
        """Test that Django test framework is working"""
        self.assertTrue(True)

    @unittest.skip("Failing test")
    def test_fail(self):
        """This shit will make build fail just for test"""
        self.assertTrue(False)
