import keyboard
import time
import mss

note_highway = {"top": 770, "left": 950, "width": 1, "height": 1}
spool = {"top": 896, "left": 1858, "width": 1, "height": 1}

def get_note_highway_pixel_color():
    img=mss.mss().grab(note_highway)
    b,g,r,a=img.raw
    return (r,g,b)

def get_spool_pixel_color():
    img=mss.mss().grab(spool)
    b,g,r,a=img.raw
    return (r,g,b)

while True:
    note_highway_color = get_note_highway_pixel_color()
    spoolcolor = get_spool_pixel_color()

    if note_highway_color == (0, 255, 0) and spoolcolor == (51, 51, 51):
        keyboard.press_and_release('space')