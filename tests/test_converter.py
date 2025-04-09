import os
import unittest
from pdb2crd.converter import convert_pdb_to_crd, save_crd

class TestPDBToCRD(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data_dir = os.path.join(os.path.dirname(__file__), "test_data")
        cls.sample_pdb = os.path.join(cls.test_data_dir, "sample.pdb")
        cls.expected_crd = os.path.join(cls.test_data_dir, "expected_output.crd")
        cls.output_crd = os.path.join(cls.test_data_dir, "temp_output.crd")

    def test_convert_pdb_to_crd(self):
        """Test conversion from PDB to CRD string"""
        with open(self.expected_crd, 'r') as f:
            expected = f.read().strip()
        
        result = convert_pdb_to_crd(self.sample_pdb).strip()
        self.assertEqual(result, expected)

    def test_save_crd(self):
        """Test saving CRD to file"""
        try:
            # Test file creation
            output_path = save_crd(self.sample_pdb, self.output_crd)
            self.assertTrue(os.path.exists(output_path))
            
            # Verify content matches
            with open(output_path, 'r') as f:
                saved_content = f.read().strip()
            with open(self.expected_crd, 'r') as f:
                expected = f.read().strip()
            
            self.assertEqual(saved_content, expected)
        finally:
            # Clean up
            if os.path.exists(self.output_crd):
                os.remove(self.output_crd)

    def test_invalid_pdb_handling(self):
        """Test error handling for malformed PDB files"""
        malformed_pdb = os.path.join(self.test_data_dir, "malformed.pdb")
        
        # Create a bad PDB file
        with open(malformed_pdb, 'w') as f:
            f.write("HETATM    BAD  DATA  HERE\n")
        
        try:
            with self.assertRaises(ValueError):
                convert_pdb_to_crd(malformed_pdb)
        finally:
            if os.path.exists(malformed_pdb):
                os.remove(malformed_pdb)

    def test_empty_file(self):
        """Test handling of empty PDB files"""
        empty_pdb = os.path.join(self.test_data_dir, "empty.pdb")
        open(empty_pdb, 'w').close()  # Create empty file
        
        try:
            with self.assertRaises(ValueError):
                convert_pdb_to_crd(empty_pdb)
        finally:
            if os.path.exists(empty_pdb):
                os.remove(empty_pdb)

if __name__ == "__main__":
    unittest.main()