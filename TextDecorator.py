import tkinter as tk
from typing import List

class TextDecorator():
    def __init__(self, text_area: tk.Text):
        self.text_area = text_area
        self.config_tags()

    def fill(self, text: List[str]):
        self.text_area.configure(state="normal")
        self.text_area.delete("1.0", "end")
        for line in text:
            if "#" in line:
                self.text_area.insert("end", "\n" + line + "\n", "green")
            else:
                self.text_area.insert("end", line + "\n")

        self.text_area.configure(state="disabled")

    def placeholder(self):
        self.text_area.configure(state="normal")
        self.text_area.delete("1.0", "end")
        self.text_area.insert("end", "Generating...")
        self.text_area.configure(state="disabled")
    
    def config_tags(self):
        self.text_area.tag_config("green", foreground="green")
        self.text_area.tag_config("white", foreground="white")