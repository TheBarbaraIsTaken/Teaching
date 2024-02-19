import customtkinter as ctk
from tkinter import filedialog
import json
from test import Tester


RED = "#8B0000"
DARK_RED = "#530000"
GRAY = "gray"
DARK_GRAY = "#5A5A5A"

json_file = "text.json"
dictionary = json.load(open(json_file, "r"))
lang = "hu"


class ActionFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0), weight=1)
        self.n = 2

        self.button = ctk.CTkButton(self, text=dictionary["file"][lang], command=self.new_repo)
        self.button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    def new_repo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        
        if file_path:
            result = self.master.tester.run_tests(file_path)
            print(file_path)
            print(result)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.geometry("600x500")
        self.title(dictionary["title"][lang])
        self.grid_columnconfigure((0), weight=1)

        # Model
        self.tester = Tester()
        

        # Widgets
        self.actions = ActionFrame(self)
        self.actions.grid(row=0, column=0, padx=30, pady=(20, 15), sticky="ew", rowspan=1)                                                         
