# test_nimbuskite.py
"""
Tests for NimbusKite module.
"""

import unittest
from nimbuskite import NimbusKite

class TestNimbusKite(unittest.TestCase):
    """Test cases for NimbusKite class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NimbusKite()
        self.assertIsInstance(instance, NimbusKite)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NimbusKite()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
