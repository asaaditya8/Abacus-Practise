import tkinter as tk

window = tk.Tk()

window.title("My APP")

window.geometry("400x400")

#LABEL
title = tk.Label(text="Hello world!", font=("Times New Roman", 20))
title.grid(column=0, row=0)

button1 = tk.Button(text="Click me!", bg="red")
button1.grid(column=0, row=1)

entry_field = tk.Entry()
entry_field.grid()

window.mainloop()