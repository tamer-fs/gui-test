import customtkinter as ctk
import tkinter as tk 


class Menu:
    def __init__(self, master: ctk.CTk | ctk.CTkToplevel):
        self.master = master
        
        self.menu_font = ('', 12)
        self.menu_bar = tk.Menu(master=self.master)
        
        # file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        
        self.file_menu.add_command(
            label="Input File",
            underline=0,
            font=self.menu_font
        )
        
        self.file_menu.add_command(
            label="Output Directory",
            underline=0,
            font=self.menu_font
        )
        
        self.file_menu.add_separator()
        
        self.file_menu.add_command(
            label="Exit",
            underline=1,
            font=self.menu_font
        )
        self.menu_bar.add_cascade (
            label="File", menu=self.file_menu, underline=0, font=self.menu_font
        )
        
        # Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command (
            label="Activate Terra PDF",
            underline=0,
            font=self.menu_font
        )
        self.menu_bar.add_cascade(
            label="Help", menu=self.help_menu, underline=0, font=self.menu_font
        )
        
        # bind menu to app
        self.master.configure(menu=self.menu_bar)