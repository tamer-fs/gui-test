import customtkinter as ctk
from customtkinter.windows.widgets.scaling import ScalingTracker
from typing import Optional, Tuple, Union


class AlertTopLevel(ctk.CTkToplevel):
    def __init__(
        self, 
        *args, 
        title: str,
        text: str,
        button_text: str = 'OK',
        width: int = 450,
        height: int = 150,
        fg_color: Optional[Union[str, Tuple[str, str]]] = None, 
        **kwargs
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        
        # configure title
        self.title(title)
        
        # configure window size and location
        window_scaling = ScalingTracker.get_window_scaling(self)
        x = int(self.winfo_screenwidth() / 2 * window_scaling - width / 2)
        y = int(self.winfo_screenheight() / 2 * window_scaling - height / 2)
        self.geometry(f"{int(width / window_scaling)}x{int(height / window_scaling)}+{x}+{y}")
        self.resizable(False, False)
        
        # configure grid
        self.grid_rowconfigure([0], weight=1)
        self.grid_columnconfigure([0], weight=1)
        
        # message
        self.message_label = ctk.CTkLabel(self, text=text)
        self.message_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 0), sticky="nswe")
        
        self.close_button = ctk.CTkButton(self, text="close", command=self.destroy)
        self.close_button.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))
        
        # prevent using app
        self.grab_set()
        