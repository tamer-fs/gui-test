import sys
from terra.config import DEBUG
from terra.gui.app import App 

if not DEBUG:
    sys.tracebacklimit = 0

def run():
    app = App()
    app.mainloop()