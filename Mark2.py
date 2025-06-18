import time
import pyperclip
import pyautogui
import random
import tkinter.messagebox as messagebox
import threading
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#Mistake Mapping
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

#Typing Simulation
def simulate_typing(text, min_delay=0.05, max_delay=0.15, mistake_chance=0.037, pause_chance=0.3):
    global stop_flag
    stop_flag = False
    for char in text:
        if stop_flag:
            print("Typing stopped")
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

#Control Logic
def start_typing():
    text = pyperclip.paste()
    if not text.strip():
        messagebox.showwarning("Empty Clipboard", "Please copy some text first.")
        return
    messagebox.showinfo("Typing will begin", "Switch to the target window within 5 seconds.")
    time.sleep(5)
    simulate_typing(text)
    messagebox.showinfo("Done", "Typing completed.")

def on_start():
    threading.Thread(target=start_typing).start()

def on_stop():
    global stop_flag
    stop_flag = True

#GUI Setup 
app = ttk.Window(themename="darkly")  # You can try 'darkly', 'cyborg', 'solar', 'superhero'
app.title("The Copier")
app.geometry("400x260")
app.resizable(False, False)

title = ttk.Label(app, text="Typing Simulator", font=("Segoe UI", 16, "bold"))
title.pack(pady=(20, 5))

desc = ttk.Label(app, text="Copy some text and click Start to simulate typing.\nClick Stop anytime to interrupt.",
                 font=("Segoe UI", 11), justify="center")
desc.pack(pady=(0, 20))

start_btn = ttk.Button(app, text="Start Typing", bootstyle=SUCCESS, command=on_start, width=25)
start_btn.pack(pady=5)

stop_btn = ttk.Button(app, text="Stop Typing", bootstyle=DANGER, command=on_stop, width=25)
stop_btn.pack(pady=5)

footer = ttk.Label(app, text="Created with ❤ by Rehyann Saini", font=("Segoe UI", 9))
footer.pack(pady=(20, 10))

app.mainloop()
