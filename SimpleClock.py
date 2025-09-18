from tkinter import *
import time


def update_time ():
    string_time = time.strftime('%H:%M:%S %p')
    digital_clock.config(text=string_time)
    digital_clock.after(1000, update_time)

root = Tk()
root.title("Digital Clock")
root["bg"] = "red"

digital_clock = Label(root, font=('calibri', 40, 'bold'), bg="black", fg="green", )
digital_clock.pack(pady= 0, expand=1)

update_time()

root.mainloop()
