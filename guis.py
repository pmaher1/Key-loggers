import tkinter as tk
from constants import (
    TITLE,
    MAIN_COLOUR,
    SECONDARY_COLOUR,
    TERTIARY_COLOUR
)


class GraphicalInterface:
    """ A basic graphical interface for EndOfDayz. """

    def __init__(self, root, size, **kwargs):
        """ Constructor for BasicGraphicalInterface.

        Parameters:
            root (tk.Tk | tk.Frame): The master frame for this Frame.
            size (int): The number of rows (and height) in the map.
        """
        self._root = root
        self._size = size

        self._container = tk.Frame(root)
        self._container.pack()

        self._add_title()
        # self._set_up_view()

        # Menu

        self._step_event = None
        self._running = True

    def _add_title(self):
        """ Configure the window title and add a new title label. """
        self._root.title(TITLE)

        tk.Label(
            self._container,
            text=TITLE,
            bg=SECONDARY_COLOUR,
            relief=tk.RAISED,
            fg=MAIN_COLOUR,
            font=('Arial', 28)
        ).pack(fill=tk.X)
