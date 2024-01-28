import tkinter as tk
import threading

from Model import Model
from TextDecorator import TextDecorator

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.model = Model()
        self.TextDecorator = TextDecorator(self.text_area_output)

    def create_widgets(self):
        self.text_areas = tk.Frame(self)
        self.text_areas.pack(pady=10, padx=10, side="top")

        self.text_area_input = tk.Text(self.text_areas, undo=True, font=("Consolas", 14), height=50)
        self.text_area_input.pack(side="left")

        self.text_area_output = tk.Text(self.text_areas, state="disabled", font=("Consolas", 14), height=50)
        self.text_area_output.pack(side="right")

        self.buttons = tk.Frame(self)
        self.buttons.pack(pady=10, side="bottom")

        self.generate_button = tk.Button(self.buttons, text="  Generate  ", command=self.generate)
        self.generate_button.pack(side="left", expand=True)

        self.copy_button = tk.Button(self.buttons, text="  Copy  ", command=self.copy,)
        self.copy_button.pack(side="right", expand=True)

    def generate(self):
        self.TextDecorator.placeholder()
        
        threading.Thread(target=self.generate_async).start()

    def generate_async(self):
        response = self.model.ask(self.text_area_input.get("1.0", "end-1c"))
        
        self.master.after(0, self.TextDecorator.fill, response)
        
    def copy(self):
        self.clipboard_clear()
        self.clipboard_append(self.text_area_output.get("1.0", "end-1c"))


def main():
    root = tk.Tk()
    root.title("Python Code Comment Generator")
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()