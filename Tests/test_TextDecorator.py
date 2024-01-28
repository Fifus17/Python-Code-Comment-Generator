import unittest
import tkinter as tk

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from TextDecorator import TextDecorator

class TestTextDecorator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.text_area = tk.Text(self.root)
        self.decorator = TextDecorator(self.text_area)

    def test_fill(self):
        text = ["Hello", "# World"]
        self.decorator.fill(text)
        self.assertEqual(self.text_area.get("1.0", "end-1c"), "Hello\n\n# World\n")

    def test_placeholder(self):
        self.decorator.placeholder()
        self.assertEqual(self.text_area.get("1.0", "end-1c"), "Generating...")

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()