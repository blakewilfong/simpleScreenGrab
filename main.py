import os
import sys
import tkinter as tk
import mss
from PIL import Image
import win32clipboard
import io


def copy_image_to_clipboard(image: Image.Image):

    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  # Strip 14-byte BMP header
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()



if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class simpleScreenGrab:
    def __init__(self):
        with mss.mss() as sct:
            virtual_monitor = sct.monitors[0]  # monitor[0] = all monitors
            self.screen_width = virtual_monitor["width"]
            self.screen_height = virtual_monitor["height"]
            self.offset_x = virtual_monitor["left"]
            self.offset_y = virtual_monitor["top"]

        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+{self.offset_x}+{self.offset_y}")
        self.root.attributes("-alpha", 0.3)
        self.root.configure(bg="black")

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.canvas = tk.Canvas(self.root, cursor="cross", bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.root.bind("<Escape>", self.cancel_snip)

        self.root.mainloop()

    def cancel_snip(self, event=None):
        self.root.destroy()

    def on_mouse_down(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y,
            outline="blue", width=2
        )

    def on_mouse_drag(self, event):
        cur_x, cur_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_mouse_up(self, event):
        end_x, end_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.root.destroy()

        x1, y1 = min(self.start_x, end_x), min(self.start_y, end_y)
        x2, y2 = max(self.start_x, end_x), max(self.start_y, end_y)

        with mss.mss() as sct:
            monitor = {
                "top": int(y1) + self.offset_y,
                "left": int(x1) + self.offset_x,
                "width": int(x2 - x1),
                "height": int(y2 - y1),
            }
            sct_img = sct.grab(monitor)
            screenshot = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

        screenshot.save(os.path.join(BASE_DIR, "last_capture.png"))
        copy_image_to_clipboard(screenshot)

if __name__ == "__main__":
    simpleScreenGrab()
