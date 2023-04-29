from Notes.UI.Menu import Menu
from Notes.Core import commands


class Controller:
    def __init__(self):
        self.ui = Menu()
        self.core = commands

    def run(self):
        self.ui.intro()
