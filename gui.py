from pathlib import Path
from tkinter import *
import webbrowser
import pynput.mouse
from pynput.keyboard import Key, Controller
import keyboard
import time
from PIL import ImageGrab
import pytesseract, pyperclip
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(0)
import pyautogui as pad

open_web = True
letterwise = False

click = []
x1,x2,y1,y2 = 0,0,0,0

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"A:\Python\AutoTyping\New folder\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def share(a):
    if a == 1:
        webbrowser.open("https://github.com/TirthrajSG?tab=repositories")
    if a == 2:
        webbrowser.open("https://www.youtube.com/@indianprayers6091")
    if a == 3:
        webbrowser.open("https://www.instagram.com/tirthrajsg/")

def on_click(x, y, button, pressed):
    global x1
    global x2
    global y1
    global y2
    global click
    if len(click) >= 2:
        click = []
        return False
    if pressed and button == pynput.mouse.Button.left:
        click.append((x,y))
        if (len(click) == 1):
            x1,y1 = x,y
        if (len(click) == 2):
            x2,y2 = x,y

def on_read_click():
    if open_web:
        webbrowser.open('https://10fastfingers.com/typing-test/english')
    else:
        window.iconify()
    with pynput.mouse.Listener(on_click=on_click) as listener:
        listener.join()
    
    log.config(state='normal')
    log.insert(END, f'Co-ordinates set: ({x1},{y1}) to ({x2}, {y2})\n')
    log.config(state='disabled')
    window.focus_force()
    

def start():
    window.iconify()
    time.sleep(1)

    while True:
        if keyboard.is_pressed('`'):
            break
        img = ImageGrab.grab()
        img = img.crop((x1,y1,x2,y2))


        text = pytesseract.image_to_string(img)
        text = text.replace('\r', '').replace('\n', '')
        if text == '': break
        log.config(state='normal')
        log.insert(END, f'{text}\n')
        log.config(state='disabled')
        if not letterwise:
            for word in text.split():
                if keyboard.is_pressed('`'):
                    break
                pyperclip.copy(word)
                pad.hotkey('ctrl', 'v')
                pad.press(' ')

            pad.press(' ')
            time.sleep(0.01)
        else:
            for letter in text:
                pad.press(letter)
            pad.press(' ')
            time.sleep(0.01)

def toggle_set_2():
    global letterwise
    if letterwise: letterwise = False
    else: letterwise = True
    toggle2.config(text=f"Letterwise : {str(letterwise)}")
    log.config(state='normal')
    log.insert(END, f'Letterwise set: {str(letterwise)}\n')
    log.config(state='disabled')

def toggle_set_1():
    global open_web
    if open_web : open_web = False
    else: open_web = True
    toggle1.config(text=f"Open Website : {str(open_web)}")
    log.config(state='normal')
    log.insert(END, f'Open Web set: {str(open_web)}\n')
    log.config(state='disabled')

def show_settings():
    global toggle1
    global toggle2

    set_win = Toplevel(window)
    set_win.grab_set()
    set_win.title("Settings")
    set_win.resizable(0,0)
    set_win.geometry('337x163')
    set_win.config(bg='#9CE5F8')

    lbl1 = Label(set_win,text = 'Settings',bg='#094656', fg='white', font=('Georgia', 20))
    lbl1.place(x=0,y=0,height=40, width=337)

    open_web = True
    toggle1 = Button(set_win, command=lambda: toggle_set_1(),text=f"Open Website : {str(open_web)}", activeforeground='white',activebackground='#3A7FC8',bg='#3A7FC8', fg='white', font=('Georgia', 16))
    toggle1.place(x =25, y=54, width=286, height=34)
    
    letterwise = False
    toggle2 = Button(set_win, command=lambda: toggle_set_2(),text=f"Letterwise : {str(letterwise)}", activeforeground='white',activebackground='#3A7FC8',bg='#3A7FC8', fg='white', font=('Georgia', 16))
    toggle2.place(x =25, y=100, width=286, height=34)






window = Tk()

window.geometry("501x420")
window.configure(bg = "#9CE5F7")


canvas = Canvas(
    window,
    bg = "#9CE5F7",
    height = 420,
    width = 501,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    250.5,
    250.5,
    image=entry_image_1
)
log = Text(
    bd=0,
    bg="#397EC8",
    fg="#ffffff",
    highlightthickness=0
)
log.place(
    x=42.0,
    y=148.0,
    width=417.0,
    height=203.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    250.0,
    22.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    activebackground='#9ce5f7',
    command=lambda: share(3),
    relief="flat"
)
button_1.place(
    x=288.0,
    y=363.0,
    width=50.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    activebackground='#9ce5f7',
    highlightthickness=0,
    command=lambda: share(2),
    relief="flat"
)
button_2.place(
    x=225.0,
    y=363.0,
    width=50.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    activebackground='#9ce5f7',
    command=lambda: share(1),
    relief="flat"
)
button_3.place(
    x=162.0,
    y=363.0,
    width=50.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    activebackground='#3a7fc8',
    command=lambda: start(),
    relief="flat"
)
button_4.place(
    x=254.0,
    y=68.0,
    width=205.0,
    height=65.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    activebackground='#3a7fc8',
    command=lambda: on_read_click(),
    relief="flat"
)
button_5.place(
    x=20.0,
    y=68.0,
    width=227.0,
    height=65.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    activebackground='#094656',
    command=lambda: show_settings(),
    relief="flat"
)
button_6.place(
    x=5.0,
    y=5.0,
    width=35.0,
    height=35.0
)
window.resizable(False, False)
window.mainloop()
