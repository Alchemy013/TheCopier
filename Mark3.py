import time
import pyperclip
import pyautogui
import random
import tkinter.messagebox as messagebox
import threading
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sys
import os

keyboard_neighbors = {
    'a': ['s', 'q', 'w', 'z'], 'b': ['v', 'g', 'h', 'n'], 'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'x', 'c'], 'e': ['w', 's', 'd', 'r'], 'f': ['d', 'r', 't', 'g', 'c', 'v'],
    'g': ['f', 't', 'y', 'h', 'v', 'b'], 'h': ['g', 'y', 'u', 'j', 'b', 'n'], 'i': ['u', 'j', 'k', 'o'],
    'j': ['h', 'u', 'i', 'k', 'n', 'm'], 'k': ['j', 'i', 'o', 'l', 'm'], 'l': ['k', 'o', 'p'],
    'm': ['n', 'j', 'k'], 'n': ['b', 'h', 'j', 'm'], 'o': ['i', 'k', 'l', 'p'], 'p': ['o', 'l'],
    'q': ['a', 's', 'w'], 'r': ['e', 'd', 'f', 't'], 's': ['a', 'w', 'e', 'd', 'x', 'z'],
    't': ['r', 'f', 'g', 'y'], 'u': ['y', 'h', 'j', 'i'], 'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 'a', 's', 'e'], 'x': ['z', 's', 'd', 'c'], 'y': ['t', 'g', 'h', 'u'],
    'z': ['a', 's', 'x'], ' ': [' ']
}

stop_flag = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def simulate_typing(text, min_delay=0.05, max_delay=0.15, mistake_chance=0.037, pause_chance=0.3):
    global stop_flag
    stop_flag = False
    total_chars = len(text)
    start_time = time.time()
    for i, char in enumerate(text):
        if stop_flag:
            return
        lower_char = char.lower()
        is_alpha = lower_char in keyboard_neighbors
        if is_alpha and random.random() < mistake_chance:
            wrong_char = random.choice(keyboard_neighbors[lower_char])
            if char.isupper():
                wrong_char = wrong_char.upper()
            pyautogui.write(wrong_char)
            time.sleep(random.uniform(min_delay, max_delay))
            time.sleep(random.uniform(0.2, 0.4))
            pyautogui.press('backspace')
            time.sleep(random.uniform(0.05, 0.1))
        pyautogui.write(char)
        time.sleep(random.uniform(min_delay, max_delay))
        if char == '\n' and random.random() < pause_chance:
            time.sleep(random.uniform(3.0, 7.0))
        elif char in '.!?':
            if random.random() < 0.4:
                time.sleep(random.uniform(0.6, 1.5))
        progress_var.set((i + 1) / total_chars * 100)
        progress_bar.update()
    duration = time.time() - start_time
    show_completion_popup(duration)

def show_countdown_popup(seconds=5, on_finish=None):
    popup = ttk.Toplevel()
    popup.title("Get Ready")
    popup.geometry("300x130")
    popup.resizable(False, False)
    popup.attributes("-topmost", True)
    popup.grab_set()
    try:
        popup.iconbitmap(resource_path("rickroll.ico"))
    except Exception:
        pass
    msg = ttk.Label(popup, text="Switch to the target window...", font=("Segoe UI", 11))
    msg.pack(pady=(15, 5))
    countdown_label = ttk.Label(popup, text="", font=("Segoe UI", 12, "bold"))
    countdown_label.pack(pady=(0, 10))
    progress = ttk.Progressbar(popup, maximum=seconds, length=200, mode="determinate", bootstyle=INFO)
    progress.pack(pady=(5, 10))
    def update_countdown(t):
        if t >= 0:
            countdown_label.config(text=f"Starting in {t} seconds")
            progress['value'] = seconds - t
            popup.after(1000, update_countdown, t - 1)
        else:
            popup.destroy()
            if on_finish:
                threading.Thread(target=on_finish).start()
    update_countdown(seconds)

def show_completion_popup(duration):
    popup = ttk.Toplevel()
    popup.title("Typing Complete")
    popup.geometry("300x130")
    popup.resizable(False, False)
    popup.attributes("-topmost", True)
    popup.grab_set()
    try:
        popup.iconbitmap(resource_path("rickroll.ico"))
    except Exception:
        pass
    label1 = ttk.Label(popup, text="Typing Completed!", font=("Segoe UI", 13, "bold"))
    label1.pack(pady=(15, 5))
    label2 = ttk.Label(popup, text=f"Time Elapsed: {duration:.2f} seconds", font=("Segoe UI", 11))
    label2.pack(pady=(0, 15))
    ok_button = ttk.Button(popup, text="OK", command=popup.destroy, bootstyle=SUCCESS)
    ok_button.pack(pady=(0, 10))

def start_typing():
    text = pyperclip.paste()
    if not text.strip():
        messagebox.showwarning("Empty Clipboard", "Please copy some text first.")
        return
    progress_var.set(0)
    progress_bar.update()
    def delayed_typing():
        simulate_typing(text)
    app.after(0, show_countdown_popup, 5, delayed_typing)

def on_start():
    start_typing()

def on_stop():
    global stop_flag
    stop_flag = True

app = ttk.Window(themename="darkly")
app.title("The Copier")
app.geometry("400x300")
app.resizable(False, False)
try:
    app.iconbitmap(resource_path("rickroll.ico"))
except Exception:
    pass

title = ttk.Label(app, text="Typing Simulator", font=("Segoe UI", 16, "bold"))
title.pack(pady=(20, 5))
desc = ttk.Label(app, text="Copy some text and click Start to simulate typing.\nClick Stop anytime to interrupt.", font=("Segoe UI", 11), justify="center")
desc.pack(pady=(0, 15))
start_btn = ttk.Button(app, text="Start Typing", bootstyle=SUCCESS, command=on_start, width=25)
start_btn.pack(pady=5)
stop_btn = ttk.Button(app, text="Stop Typing", bootstyle=DANGER, command=on_stop, width=25)
stop_btn.pack(pady=5)
progress_var = ttk.DoubleVar()
progress_bar = ttk.Progressbar(app, variable=progress_var, length=300, mode='determinate', bootstyle=INFO)
progress_bar.pack(pady=(20, 10))
footer = ttk.Label(app, text="Created with ❤ by Rehyann Saini", font=("Segoe UI", 9))
footer.pack(pady=(10, 5))
app.mainloop()
