# Print the name and bounding box (x1, y1, x2, y2) for the active window in
# a loop.

import time
from collections import namedtuple

import Xlib
import Xlib.display


disp = Xlib.display.Display()
root = disp.screen().root

NET_ACTIVE_WINDOW = disp.intern_atom('_NET_ACTIVE_WINDOW')
winPos = namedtuple('winPos', 'x y height width')


def get_active_window():
    win_id = root.get_full_property(NET_ACTIVE_WINDOW,
                                    Xlib.X.AnyPropertyType).value[0]
    try:
        return disp.create_resource_object('window', win_id)
    except Xlib.error.XError:
        pass


def get_absolute_geometry(win):
    """
    Returns the (x, y, height, width) of a window relative to the top-left
    of the screen.
    """
    geom = win.get_geometry()
    (x, y) = (geom.x, geom.y)
    while True:
        parent = win.query_tree().parent
        pgeom = parent.get_geometry()
        x += pgeom.x
        y += pgeom.y
        if parent.id == root.id:
            break
        win = parent
    return winPos(x, y, geom.height, geom.width)
