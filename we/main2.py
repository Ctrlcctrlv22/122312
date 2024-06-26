from tkinter import *

root = Tk()
root.title("app")
root.geometry("700x600")

ent = Entry(font=('Comic Sans MS', 16, "bold"))
ent.pack()

label = Label(text='')
label.pack()

def click_button():
    val = ent.get()
    label["text"] = val

btn = Button(text='click meeee', command=click_button)
btn.pack()

root.mainloop()