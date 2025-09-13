from tkinter import ttk
from tkinter import *


app = Tk()
app.title("app button scrollbar modify")
app.geometry("800x100")
app["bg"] = "darkred"




lab = Label(app, bg="black", border=3 )
lab.place(relx=0.5, rely=0.5, anchor="center")

main_frame = Frame(lab)
main_frame.pack(fill=BOTH, expand=1)


#canvas = size
my_canvas = Canvas(main_frame, width=750, height=55, bg="green", border=-5)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

style = ttk.Style()
style.theme_use('clam')
style.configure("TScrollbar", gripcount=0, background="yellowgreen", troughcolor="green", bordercolor="black", lightcolor="yellowgreen", darkcolor="yellowgreen", arrowcolor="black")
style.map('TScrollbar', background=[('active', 'green')], lightcolor=[('active', 'black')], darkcolor=[('active', 'black')])

my_scrollbar = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
my_scrollbar.place(relx=0.5, rely=1, anchor="s", width=750, height=13)




my_canvas.config(xscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.config(scrollregion=my_canvas.bbox("1")))

second_frame = Frame(my_canvas, bg="green")

my_canvas.create_window((0,0), window=second_frame, anchor="ne")


for thing in range(100):
    Button(second_frame, text=f"it's Button {thing}yo!", bg="yellowgreen", activebackground="green", border=0).grid(row=0, column=thing, pady=5, padx=5)


app.mainloop()


#, gripcount=0,
#                bg="black", darkcolor="black", lightcolor="black",
#                troughcolor="black", arrowcolor="black",
