import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


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

"""
Instead of using box, use LABEL
color can be changed + similar to image load in pygame """

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title = "2048 Game") # use super as it is used in python3
        self.set_size_request(400,400)
        self.connect('delete-event', Gtk.main_quit)

    def display_button (self,board):
        grid = Gtk.Grid()
        self.add(grid)
        button = Gtk.Button(label = 'NEW GAME') # use button.set_label when developing UI in code
        grid.attach(button, 2, 0, 2, 1)
        for row in range (0,len(board)):
            for col in range (0,len(board)):
                    button = Gtk.Button(label = str(board[row][col]))
                    grid.attach(button, col, row + 1, 1, 1) # use relative positions

        grid.set_column_homogeneous(True)
        grid.set_column_spacing(10)
        grid.set_row_homogeneous(True)
        grid.set_row_spacing(10)

    def on_key_press_event(self, widget, event):
        pass

    def update_label_text(self):
        pass

board = [[0 for i in range (4)] for j in range (4)]
