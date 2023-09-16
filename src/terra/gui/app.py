import customtkinter as ctk
from customtkinter.windows.widgets.scaling import ScalingTracker

from terra.gui.frames.split import SplitFrame
from terra.gui.menu import Menu

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # configure title
        self.title("terra PDF")
        
        # bind menu bar
        self.menu = Menu(self)
        
        # configure window size & location
        window_scaling = ScalingTracker.get_widget_scaling(self)
        widget_width = 700
        widget_height = 190
        x = int(self.winfo_screenwidth() / 2 * window_scaling - widget_width / 2)
        y = int(self.winfo_screenheight() / 2 * window_scaling - widget_height / 2)
        self.geometry(
            f"{int(widget_width / window_scaling)}x{(int(widget_height / window_scaling))}+{x}+{y}"
        )
        self.resizable(False, False)
        
        # configure grid
        self.grid_rowconfigure([0], weight=1)
        self.grid_columnconfigure([0], weight=1)
        
        # Interface frames
        self.split_frame = SplitFrame(self)
        self.split_frame.grid(row=0, column=0, sticky="nswe")
        
        # TODO: remove after testing
        from terra.gui.toplevels.alert import AlertTopLevel
        AlertTopLevel(self, title="Test", text="Your pc will explode")