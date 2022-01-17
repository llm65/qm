import tkinter
from tkinter import messagebox
from time import sleep, localtime

root = tkinter.Tk()
root.withdraw()

while True:
    t = localtime()
    if t.tm_hour == 11 and t.tm_min == 30:
        for i in range(7):
            messagebox.showinfo('提示', '喝茶')
            sleep(3600)
        break
    sleep(60)
