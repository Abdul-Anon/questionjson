from tkinter import *
import tkinter.ttk as ttk

win = Tk()
win.geometry('620x520')
win.title('Find LCM AND HCF')
win.maxsize(620, 520)
win.minsize(620, 520)

# try:
# except:
# 	pass
	
label = ttk.Label(win)
label.place(relwidth=1, relheight=1)

# Frame
frame1 = ttk.Frame(label)
frame1.place(relwidth= 0.4, relheight=0.1, relx=0.05, rely=0.01)
frame2 = ttk.Frame(label)
frame2.place(relwidth= 0.4, relheight=0.1, relx=0.05, rely=0.12)
frame3 = ttk.Frame(label)
frame3.place(relx=0.48, rely=0.01, relwidth=0.2, relheight=0.21)
frame4 = Entry(label)
frame4.place(relwidth= 0.9, relheight=0.7)
frame6 = ttk.Frame(label)
frame6.place(relx=0.7, rely=0.01, relwidth=0.2, relheight=0.21)

# Label
label1 = ttk.Label(frame1, text='Number:')
label1.place(relheight=1, relwidth=0.3)
label2 = ttk.Label(frame2, text='Number:')
label2.place(relheight=1, relwidth=0.3)

# Entry
entry1 = ttk.Entry(frame1, width=251, font=8)
entry1.place(relheight=1, relx=0.3)
entry2 = ttk.Entry(frame2, width=251, font=8)
entry2.place(relheight=1, relx=0.3)

# Button
button1 = ttk.Button(frame3, text='Find LCM')
button1.place(relwidth=1, relheight=1)
button2 = ttk.Button(frame6, text='Find HCF')
button2.place(relwidth=1, relheight=1)

win.mainloop()