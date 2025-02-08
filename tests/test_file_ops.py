# Copyright (c) 2025 Ernesto Sola-Thomas

"""
Test module for file operations functionality.
"""

import unittest
from pathlib import Path
import tempfile
import os

from src import file_ops

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp()
        self.test_content = b"Test content for file operations"
        self.test_file = Path(self.test_dir) / "test.txt"
        self.test_file.write_bytes(self.test_content)
        
    def tearDown(self):
        """Clean up test environment."""
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)
        
    def test_read_file(self):
        """Test reading file contents."""
        content = file_ops.read_file(str(self.test_file))
        self.assertEqual(content, self.test_content)
        
    def test_write_read_encrypted_file(self):
        """Test writing and reading encrypted file."""
        # Test data
        encrypted_content = b"encrypted_content"
        ciphertext = b"ciphertext"
        metadata = {"version": "1.0", "algorithm": "test"}
        
        # Write encrypted file
        encrypted_path = file_ops.write_encrypted_file(
            str(self.test_file),
            encrypted_content,
            ciphertext,
            metadata
        )
        
        # Verify file exists
        self.assertTrue(os.path.exists(encrypted_path))
        
        # Read encrypted file
        read_content, read_ciphertext, read_metadata = file_ops.read_encrypted_file(encrypted_path)
        
        # Verify contents
        self.assertEqual(read_content, encrypted_content)
        self.assertEqual(read_ciphertext, ciphertext)
        self.assertEqual(read_metadata, metadata)
        
if __name__ == '__main__':
    unittest.main() 