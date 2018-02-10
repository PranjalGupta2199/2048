import gi
from packages import gui
#from packages import key_function as func
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gtk, Gdk

if __name__ == "__main__":

    Window = gui.MyWindow()
    Window.display_button()
    #Window.connect('delete-event', Gtk.main_quit)

    Window.show_all()
    Gtk.main()
