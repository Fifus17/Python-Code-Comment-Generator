import unittest
import tkinter as tk
import threading

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Application import Application

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = Application(master=self.root)

    def test_copy(self):
        self.app.text_area_output.config(state="normal")
        self.app.text_area_output.insert("1.0", "Test text")
        self.app.text_area_output.config(state="disabled")
        self.app.copy()
        self.assertEqual(self.root.clipboard_get(), "Test text")

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()