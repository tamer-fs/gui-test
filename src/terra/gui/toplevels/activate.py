import customtkinter as ctk
from customtkinter.windows.widgets.scaling import ScalingTracker
from typing import Optional, Tuple, Union

class ActivateTopLevel(ctk.CTkToplevel):
    def __init__(
        self, 
        *args, 
        width: int = 550, 
        height: int = 150, 
        fg_color: str | Tuple[str, str] | None = None, 
        **kwargs
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        
        # configure title
        self.title("Activate Terra PDF")
        
        # configure window size & location
        window_scalling = ScalingTracker.get_window_scaling(self)
        x = int(self.winfo_screenwidth() / 2 * window_scalling - width / 2)
        y = int(self.winfo_screenheight() / 2 * window_scalling - height / 2)
        self.geometry(f"{int(width / window_scalling)}x{int(height / window_scalling)}+{x}+{y}")

        # configure grid
        self.grid_rowconfigure([1], weight=1)
        self.grid_columnconfigure([1], weight=1)
        
        # licence field
        self.licence_label = ctk.CTkLabel(master=self, text="Licence key")
        self.licence_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))
        
        self.licence_entry = ctk.CTkEntry(master=self, placeholder_text="Enter licence key here")
        self.licence_entry.grid(row=0, column=1, padx=(10, 10), pady=(10, 0), sticky="nswe")
        
        # activate button
        self.activate_button = ctk.CTkButton(master=self, text="Activate")
        self.activate_button.grid(
            row=1, column=0, columnspan=2, padx=(10, 10), pady=(10, 10), sticky="we"
        )
        
        # Prevent use of app while activate window is open
        self.grab_set()