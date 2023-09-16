import customtkinter as ctk
from typing import Optional, Tuple, Union

from terra.gui import app 


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
            master=self, text=r"C:\test\test.pdf", fg_color="#515151", corner_radius=6, anchor="w"
        )
        self.input_file_path.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="we")
        
        self.input_file_button = ctk.CTkButton(master=self, text="Browse", width=70)
        self.input_file_button.grid(row=0, column=2, padx=(10, 10), pady=(10, 0))
        
        # output directory
        self.output_dir_label = ctk.CTkLabel(master=self, text="Output Folder:")
        self.output_dir_label.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), sticky="w")
        
        self.output_dir_path = ctk.CTkLabel(
            master=self, text=r"C:\test", fg_color="#515151", corner_radius=6, anchor="w"
        )
        self.output_dir_path.grid(row=1, column=1, padx=(10, 0), pady=(10, 0), sticky="we")
        
        self.output_dir_button = ctk.CTkButton(master=self, text="Browse", width=70)
        self.output_dir_button.grid(row=1, column=2, padx=(10, 10), pady=(10, 0))
        
        # action button
        self.action_button = ctk.CTkButton(master=self, text="split")
        self.action_button.grid(
            row=2, column=0, columnspan=3, padx=(10,10), pady=(10, 10), sticky="we"
        )