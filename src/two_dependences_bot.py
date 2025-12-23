import keyboard
import time
import mss

note_highway = {"top": 836, "left": 950, "width": 1, "height": 1}
spool = {"top": 905, "left": 1850, "width": 1, "height": 1}

def get_note_highway_pixel_color():
    try:
        img = mss.mss().grab(note_highway)
        b, g, r, a = img.raw
        return (r, g, b)
    except Exception as e:
        return None

def get_spool_pixel_color():
    try:
        img = mss.mss().grab(spool)
        b, g, r, a = img.raw
        return (r, g, b)
    except Exception as e:
        return None

while True:
    note_highway_color = get_note_highway_pixel_color()
    spool_color = get_spool_pixel_color()

    if note_highway_color == (0, 255, 0) and spool_color == (51, 51, 51):
        keyboard.press_and_release('space')
        time.sleep(0.14)