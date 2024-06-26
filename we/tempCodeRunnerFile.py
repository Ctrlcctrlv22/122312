btn = Button(text='Click me', command=click_button1)
btn.pack()

btn = Button(text='dont click me', command=click_button2)
btn.pack()

btn = Button(text='close', command=finish)
btn.pack()

btn = Button(text='clicks', state=["disabled"])
btn.pack()
