import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from . import key_function as func


up = func.Moves('up')
down = func.Moves('down')
right = func.Moves('right')
left = func.Moves('left')

class MyWindow(Gtk.Window):
    ButtonList = []
    l = []

    def __init__(self):
        Gtk.Window.__init__(self, title = "2048 Game") # use super as it is used in python3
        self.set_size_request(400,400)
        self.connect('delete-event', Gtk.main_quit)
        self.connect('key-press-event', self.on_key_press_event)
        self.board = [[ 0 for i in range (4)] for j in range (4)]


    def display_button (self):
        grid = Gtk.Grid()
        self.add(grid)
        button = Gtk.Button(label = 'NEW GAME') # use button.set_label when developing UI in code
        grid.attach(button, 2, 0, 2, 1)

        for row in range (0,len(self.board)):
            for col in range (0,len(self.board)):
                    button = Gtk.Button()
                    MyWindow.l.append(button)
                    grid.attach(button, col, row + 1, 1, 1) # use relative positions


                    text = self.board[row][col]
                    if text == 0:
                        text = " "
                    button.set_label(str(text))

            MyWindow.ButtonList.append(MyWindow.l)
            MyWindow.l = []


        grid.set_column_homogeneous(True)
        grid.set_column_spacing(10)
        grid.set_row_homogeneous(True)
        grid.set_row_spacing(10)


    def on_key_press_event(self, widget, event):
        keyname = Gdk.keyval_name(event.keyval)

        if keyname == "Up":  board = up.function(self.board)
        elif keyname == "Down": board = down.function(self.board)
        elif keyname == "Right": board = right.function(self.board)
        elif keyname == "Left": board = left.function(self.board)
        else: pass

        self.update_label_text()

    def update_label_text(self):
        for row in range (0, 4):
            for col in range (0,4 ):
                text = self.board[row][col]
                if text == 0:
                    text = " "
                MyWindow.ButtonList[row][col].set_label(str(text))



'''
Will use GTk.Grid object.
Gtk.Grid.attach(child,left,top,width,height)
left = column number at which it will be placed
top = row number -----''--------
width = number of columns it will span
height = number of rows it will span
'''

"""
Gtk.Grid.attach_next_to(child,sibling,side, width, height)
child = widget to be added
sibling = can be none or other child object. If it is none then it will be placed either at the begining or at the end
side = GTk.PositionType(Value) can be RIGHT = 1, LEFT = 0, TOP = 2, BOTTOM = 3
width, height = same as Gtk.Grid.attach () method
"""
