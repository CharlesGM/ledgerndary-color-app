import unittest
import os
from app import VALID_COLORS

class TestPageColor(unittest.TestCase):
    
    def test_page_color_valid(self):
        # Load the PAGE_COLOUR from the environment variable
        color = os.getenv('PAGE_COLOUR', 'white')
        
        # Check if the color is valid
        self.assertIn(color, VALID_COLORS, f"Invalid color: {color}. Must be one of: {', '.join(VALID_COLORS)}")

if __name__ == '__main__':
    unittest.main()
