import tkinter as tk
import datetime
import calendar

okno = tk.Tk()
okno.geometry("600x400")

mesec = calendar.month(datetime.datetime.now().year, datetime.datetime.now().month)
mesec = mesec.strip().split()

vrsta = 1
stolpec = 1
for dan in mesec[9:]:
    if stolpec > 7:
        stolpec = 1
        vrsta += 1
    gumb = tk.Button(okno, text="{0}".format(dan))
    gumb.grid(column=stolpec, row=vrsta)
    stolpec += 1
