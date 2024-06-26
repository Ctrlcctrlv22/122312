import tkinter as tk

def open_second_window():
    main_window.withdraw()
    second_window.deiconify()
    
def back_to_main_window():
    second_window.withdraw()
    main_window.deiconify()
    
main_window = tk.Tk()
main_window.title("Main Window")
main_window.geometry("700x600")
main_window.configure(bg='#784794')

txt = tk.Label(main_window, text = 'Main Window', font=('Comic Sans MS', 16))
txt.pack()

open_button = tk.Button(main_window, text="Open Second window", command=open_second_window)
open_button.pack(pady=20)

second_window = tk.Toplevel(main_window)
second_window.title("Second Window")
second_window.geometry("700x600")
second_window.configure(bg= "#ff0000")
second_window.withdraw()

txt = tk.Label(second_window, text='Second window', font=('Comic Sans MS', 16))
txt.pack()

back_button = tk.Button(second_window, text= "Back to main Window", command= back_to_main_window)
back_button.pack(pady=20)

main_window.mainloop()
