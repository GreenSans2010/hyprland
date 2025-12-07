import tkinter as tk
import os

window = tk.Tk()
window.geometry('99x163')
window.wm_attributes('-type', 'dialog')

def button_click_off():
    os.system("poweroff")

def button_click_reboot():
    os.system("reboot")

def button_click_suspend():
    os.system("systemctl suspend")

def button_click_lock():
    os.system("hyprlock")

button1 = tk.Button(
    text="poweroff  󰤆",
    width=10,
    height=2,
    bg="#BB582E",
    fg="#D3ECF2",
    command=button_click_off
)

button2 = tk.Button(
    text='reboot  ',
    width=10,
    height=2,
    bg="#BB582E",
    fg="#D3ECF2",
    command=button_click_reboot
)

button3 = tk.Button(
    text='suspend  ',
    width=10,
    height=2,
    bg="#BB582E",
    fg="#D3ECF2",
    command=button_click_suspend
)

button4 = tk.Button(
    text='lock  ',
    width=10,
    height=2,
    bg="#BB582E",
    fg="#D3ECF2",
    command=button_click_lock
)

button1.place(x=0, y=0)
button2.place(x=0, y=40)
button3.place(x=0, y=80)
button4.place(x=0, y=120)

window.mainloop()
