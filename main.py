from packages import gui
from packages import key_function as func
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

if __name__ == "__main__":
    up = func.Moves('up')
    down = func.Moves('down')
    right = func.Moves('right')
    left = func.Moves('left')

    Window = gui.MyWindow()
    board = [[ 0 for i in range (4)] for j in range (4)]
    Window.display_button(board)
    Window.connect('delete-event', Gtk.main_quit)

    Window.show_all()
    Gtk.main()
