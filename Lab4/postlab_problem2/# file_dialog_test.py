# file_dialog_test.py

import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # hide main window
    file_path = filedialog.askopenfilename(title="Select a text file",
                                           filetypes=[("Text files", "*.txt")])
    if file_path:
        print("Selected file:", file_path)
    else:
        print("No file selected.")

if __name__ == "__main__":
    select_file()
