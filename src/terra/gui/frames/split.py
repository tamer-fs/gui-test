import customtkinter as ctk
from typing import Optional, Tuple, Union
from tkinter import filedialog
from pathlib import Path

from terra.core import split_pdf
from terra.gui import app 
from terra.gui.toplevels.alert import AlertTopLevel


class SplitFrame(ctk.CTkFrame):
    def __init__(
        self, 
        master: any, 
        width: int = 200, 
        height: int = 200, 
        corner_radius: int | str | None = 0, 
        border_width: int | str | None = None, 
        bg_color: str | Tuple[str, str] = "transparent", 
        fg_color: str | Tuple[str, str] | None = None, 
        border_color: str | Tuple[str, str] | None = None, 
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, 
        overwrite_preferred_drawing_method: str | None = None, 
        **kwargs
    ):
        super().__init__(
            master, 
            width, 
            height, 
            corner_radius, 
            border_width, 
            bg_color, fg_color, 
            border_color, 
            background_corner_colors, 
            overwrite_preferred_drawing_method, 
            **kwargs
        )
        
        self.app: app.App = self.master.winfo_toplevel()
        
        self.grid_rowconfigure([2], weight=1)
        self.grid_columnconfigure([1], weight=1)
        
        # input file
        self.input_file_label = ctk.CTkLabel(master=self, text="Input file:")
        self.input_file_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky="w")
        
        self.input_file_path = ctk.CTkLabel(
            master=self, text="", fg_color="#515151", corner_radius=6, anchor="w"
        )
        self.input_file_path.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="we")
        
        self.input_file_button = ctk.CTkButton(master=self, text="Browse", width=70, command=lambda: self.select_input_file())
        self.input_file_button.grid(row=0, column=2, padx=(10, 10), pady=(10, 0))
        
        # output directory
        self.output_dir_label = ctk.CTkLabel(master=self, text="Output Folder:")
        self.output_dir_label.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), sticky="w")
        
        self.output_dir_path = ctk.CTkLabel(
            master=self, text="", fg_color="#515151", corner_radius=6, anchor="w"
        )
        self.output_dir_path.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky="we")
        
        self.output_dir_button = ctk.CTkButton(master=self, text="Browse", width=70, command=lambda: self.select_output_dir())
        self.output_dir_button.grid(row=1, column=2, padx=(10, 10), pady=(10, 0))
        
        # action button
        self.action_button = ctk.CTkButton(master=self, text="split", command=lambda: self.process_file())
        self.action_button.grid(
            row=2, column=0, columnspan=3, padx=(10,10), pady=(10, 10), sticky="we"
        )
        
    def select_input_file(self):
        path = filedialog.askopenfilename()
        
        if path == '':
            self.input_file_path.configure(text='')
        else:
            self.input_file_path.configure(text=Path(path))
            
    def select_output_dir(self):
        path = filedialog.askdirectory()
        
        if path == '':
            self.output_dir_path.configure(text='')
        else:
            self.output_dir_path.configure(text=Path(path))
            
    def process_file(self):
        input_file_path = self.input_file_path.cget("text")
        output_dir_path = self.output_dir_path.cget("text")
        
        # check if paths are not empty
        if input_file_path == '' or output_dir_path == '':
            AlertTopLevel(
                self.app,
                title="Path missing",
                text="Please select an input file and a output directory.",
                button_text="Close",
            )
            
        # Process pdf
        try:
            split_pdf(input_file_path, output_dir_path)
        except Exception as e:
            AlertTopLevel(
                self.app,
                title="Operation Failed",
                text=str(e),
                button_text="Close",
            )
            return
        
        # Notify user
        self.bell()
        self.action_button.configure(text="Success", fg_color='#008000')
        self.after(5000, lambda: self.action_button.configure(text="Split", fg_color="#1F6AA5"))