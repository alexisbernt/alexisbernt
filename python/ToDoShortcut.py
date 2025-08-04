import keyboard
import tkinter as tk
from threading import Thread

def show_popup():
    def popup():
        root = tk.Tk()
        root.title("To-Do")
        root.geometry("250x100")
        root.attributes('-topmost', True)  # Always on top

        label = tk.Label(root, text="Hello here is your to-do: Gmail email, budget, code/learn something")
        label.pack(pady=20)

        # Optional: auto-close after 5 seconds
        root.after(5000, root.destroy)

        root.mainloop()

    # Run in a separate thread so it doesn’t block the hotkey listener
    Thread(target=popup).start()

# Register hotkey: Shift + Alt + C
keyboard.add_hotkey('shift+alt+c', show_popup)

print("Hotkey listener running... Press SHIFT + ALT + C to show popup. Press ESC to quit.")
keyboard.wait('esc')

# Listens for Shift + Alt + C using keyboard.add_hotkey.
#
# When triggered, it shows a tkinter popup window with the message.
#
# Runs the GUI in a separate thread to keep the listener responsive.
#
# Press ESC to stop the program.