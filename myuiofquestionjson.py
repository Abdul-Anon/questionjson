from tkinter import *
from tkinter import messagebox

root = Tk()

some_label = Label(root, text="Hello, world!")
question_entry = Entry(root, width=600, font=8)
question_entry.pack()
some_label.pack()
submit_button = Button(root, text="Submit", pady=2)
submit_button.pack()
root.geometry('600x500')
root.title('Convert Questions to JSON')
root.maxsize(620, 520)
root.minsize(620, 520)

root.mainloop()
