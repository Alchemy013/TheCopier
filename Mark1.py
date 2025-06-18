import time
import pyperclip
import pyautogui
import random
import tkinter as tk
from tkinter import messagebox
import threading

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

        if char == '\n':
            if random.random() < pause_chance:
                pause_duration = random.uniform(3.0, 7.0)
                print(f"Pause {pause_duration:.2f}s ")
                time.sleep(pause_duration)
        elif char in '.!?':
            if random.random() < 0.4:
                pause_duration = random.uniform(0.6, 1.5)
                time.sleep(pause_duration)

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

root = tk.Tk()
root.title("The Copier")
root.geometry("300x200")

label = tk.Label(root, text="Copy text and click Start to simulate typing.\nClick Stop to interrupt.", wraplength=280)
label.pack(pady=10)

start_button = tk.Button(root, text="Start Typing", command=on_start, height=2, width=20)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Typing", command=on_stop, height=2, width=20)
stop_button.pack(pady=5)

root.mainloop()
