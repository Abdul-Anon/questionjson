from tkinter import *
from tkinter import messagebox

root = Tk()

some_label = Label(root, text="Hello, world!")
question_entry = Entry(root,  font=8)
question_entry.place(relheight=0.5, relwidth=0.9, x=31, y=30)
some_label.pack()
submit_button = Button(root, text="Submit", pady=2)
submit_button.place(x=300, y=475)
root.title('Convert Questions to JSON')
root.maxsize(620, 520)
root.minsize(620, 520)
root.geometry("620x520")
root.mainloop()
