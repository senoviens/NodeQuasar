# test_nodequasar.py
"""
Tests for NodeQuasar module.
"""

import unittest
from nodequasar import NodeQuasar

class TestNodeQuasar(unittest.TestCase):
    """Test cases for NodeQuasar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeQuasar()
        self.assertIsInstance(instance, NodeQuasar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeQuasar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
