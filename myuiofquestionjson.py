import os


def convert(question, a, b, c, d, answer):


    dictionary = {
        "question": question,
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "ans": answer
    }
 
    # Serializing json
    json_object = json.dumps(dictionary, indent=4)
    
    # Writing to sample.json
    with open(f"{os.path.dirname(os.path.realpath(__file__))}\question.json", "a") as outfile:
        json.dump(dictionary, outfile)
        print()




from tkinter import *
import json
from tkinter import messagebox

root = Tk()

some_label = Label(root, text="Hello, world!", fg="gold", bg="#888888", font=("Bold"))
some_label.pack()
question_entry = Entry(root, font=8, bg="#6c6c6c", fg="gold")
question_entry.place(relheight=0.38, relwidth=0.9, x=31, y=30)
possible_ans_a_label = Label(root, text="A", bg="#888888")
possible_ans_a_label.place(x=31, y=240)
possible_ans_b_label = Label(root, text="B", bg="#888888")
possible_ans_b_label.place(x=430, y=240)
possible_ans_c_label = Label(root, text="C", bg="#888888")
possible_ans_c_label.place(x=31, y=340)
possible_ans_d_label = Label(root, text="D", bg="#888888")
possible_ans_d_label.place(x=430, y=340)
answer_label = Label(root, text="Answer", bg="#888888")
answer_label.place(x=200, y=300)
possible_ans_a = Entry(root, bg="#6c6c6c", fg="gold")
possible_ans_b = Entry(root, bg="#6c6c6c", fg="gold")
possible_ans_b = Entry(root, bg="#6c6c6c", fg="gold")
possible_ans_c = Entry(root, bg="#6c6c6c", fg="gold")
possible_ans_d = Entry(root, bg="#6c6c6c", fg="gold")
answer = Entry(root, bg="#6c6c6c", fg="gold")
possible_ans_a.place(relwidth=0.2, x=50, y=240)
possible_ans_b.place(relwidth=0.2, x=449, y=240)
possible_ans_c.place(relwidth=0.2, x=50, y=340)
possible_ans_d.place(relwidth=0.2, x=449, y=340)
answer.place(relwidth=0.2, x=250, y=300)
submit_button = Button(root, text="Submit", pady=2, bg="#3a3a3a", fg="gold", command=lambda: convert(question_entry.get(), possible_ans_a.get(), possible_ans_b.get(), possible_ans_c.get(), possible_ans_d.get(), answer.get()))
submit_button.place(x=300, y=475)
root.title('Convert Questions to JSON')
root.config(bg="#888888")
root.maxsize(620, 520)
root.minsize(620, 520)
root.geometry("620x520")
root.mainloop()