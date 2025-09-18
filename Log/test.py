
from tkinter import *



def actulog():
    with open("Amodifier.txt") as f:
        log = f.read()
        logtex.config(text=log, anchor='s', justify=LEFT)
        logtex.after(1000, actulog)



app = Tk()
app.title("afichage en direct")
lfe = 500
hfe = 500
app.geometry(f"{lfe}x{hfe}")

llt = lfe*0.8
hlt = hfe*0.8

#scrolbar = Scrollbar(app)
#scrolbar.pack(side="right", fill="y")

logtex = Label(app, bg="black", fg="white")
logtex.place(relx=0.5, rely=0.5, width=llt, height=hlt, anchor="center")
actulog()



app.mainloop()
