# test_datadrift.py
"""
Tests for DataDrift module.
"""

import unittest
from datadrift import DataDrift

class TestDataDrift(unittest.TestCase):
    """Test cases for DataDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataDrift()
        self.assertIsInstance(instance, DataDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
