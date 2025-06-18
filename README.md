# 🖋️ The Copier

**The Copier** is a sleek and modern Python GUI app that simulates human typing with realism — adding delays, typos, corrections, and pauses to mimic a real person. Copy any text and it will type it out in any window for you.

![image](https://github.com/user-attachments/assets/c229e3d0-6b29-4583-975a-61b3b60007ab)

---

## ✨ Features

- ⌨️ **Simulates Human Typing** – Includes random typos and intelligent backspacing.
- 🧠 **Smart Delays** – Typing pauses at punctuation and line breaks.
- 📋 **Clipboard Integration** – Just copy and click start.
- ⏳ **Countdown Window** – Gives you time to switch to your target app.
- ✅ **Completion Summary** – Displays total typing duration.
- 🖼️ **Custom Icons** – Integrated app icon for all windows and popups.
- 🌗 **Dark Theme GUI** – Clean interface using `ttkbootstrap`.
- 💻 **Standalone Executable** – Build ready for Windows and macOS.

---

## 📦 Installation

### ▶️ Run from Source

```bash
git clone https://github.com/yourusername/TheCopier.git
cd TheCopier
pip install -r requirements.txt
python main.py
```

### 🪟 Build Windows Executable

```bash
pyinstaller --onefile --noconsole --icon=rickroll.ico --add-data "rickroll.ico;." main.py
```

### 🍎 Build macOS App

Install py2app:

```bash
pip install py2app
python setup.py py2app
```

Then bundle with:

```bash
create-dmg 'dist/The Copier.app' --overwrite --dmg-title='The Copier' --app-drop-link=150,150 TheCopier.dmg
```

---

## 🖼️ App Layout

```
TheCopier/
├── main.py             # Main script
├── rickroll.ico        # Custom icon
├── setup.py            # Mac packaging file
├── README.md
```

---

## ⚙️ Dependencies

- `pyautogui`
- `pyperclip`
- `ttkbootstrap`
- `tkinter` (standard with Python)

---

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/c229e3d0-6b29-4583-975a-61b3b60007ab)
![image](https://github.com/user-attachments/assets/06dbfea8-3b31-4e90-b0af-433be6c6ed74)
![Screenshot 2025-06-18 201459](https://github.com/user-attachments/assets/ca4c09b1-78da-45a8-969a-29fbb86d02fd)

---

## 🧪 How to Use

1. Copy any text (Ctrl+C)
2. Open **The Copier**
3. Click **Start Typing**
4. Switch to any typing-capable app
5. Watch it type automatically with pauses, typos, and flair

Click **Stop Typing** to cancel mid-run.

---

## 🛠 License

MIT License © 2025 [Rehyann Saini](https://github.com/rehyannsaini)

---

## 🙏 Acknowledgements

- Inspired by the idea of a ghost typer.
- Uses beautiful `ttkbootstrap` themes.
- Made with ❤️ and backspaces by Rehyann Saini
