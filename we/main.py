from tkinter import *


root = Tk()
root.title("Приложение")
root.geometry("700x600")
root.configure(bg="#784794")

txt = Label( text='         helllllllllllllllllllllllllllllooooooooooooooooooooooooooooooooo                 ',font=('Comic Sans Ms', 16, 'bold'), background="#784794")
txt.pack()

frame = Frame(root, bg="#784794")
frame.pack(anchor= 'center',)

def click_button1():
    root.configure(bg="#784794")  
    frame['bg']= "#784794"
    txt['bg']= "#784794"
def click_button2():
    root.configure(bg="#ff0000")
    frame['bg']= "#ff0000"
    txt['bg']= "#ff0000"
def click_button3():
    root.configure(bg="#3aed2d")
    frame['bg']= "#3aed2d"
    txt['bg']= "#3aed2d"
def click_button4():
    root.configure(bg="#6dbdb6")
    frame['bg']= "#6dbdb6"
    txt['bg']= "#6dbdb6"
    
btn = Button(frame,text= 'home', font=(16), background="#784794", command=click_button1)
btn1 = Button(frame, text= 'about', background='#ff0000', command=click_button2)
btn2 = Button(frame, text= 'shop', font=(100), background='#3aed2d', command=click_button3)
btn3 = Button(frame, text= 'profile', background='#6dbdb6', command=click_button4)

btn.grid(row=0, column=0, padx=10, pady=10)
btn1.grid(row=0, column=1, padx=10, pady=10)
btn2.grid(row=0, column=2, padx=10, pady=10)
btn3.grid(row=0, column=3, padx=10, pady=10)






root.mainloop()