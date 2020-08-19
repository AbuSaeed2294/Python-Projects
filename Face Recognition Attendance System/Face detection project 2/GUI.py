
from tkinter import *
import os

# creating instance of TK
root = Tk()

root.configure(background="black")


# root.geometry("300x300")

def function1():
    os.system('py Get_Dataset.py')


def function2():
    os.system("py training_dataSet.py")


def function3():
    os.system('py Recognizer_file.py')


def function6():
    root.destroy()


def attend():
    os.startfile('D:/Programs/Python Project/FINAL YEAR PROJECT 2/Attendance sheet/')


# stting title for the window
root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

# creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 20), fg="white", bg="black",
      height=2).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating first button
Button(root, text="Create Dataset", font=("times new roman", 20), bg="white", fg='black', command=function1).grid(
    row=3, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)

# creating second button
Button(root, text="Train Model", font=("times new roman", 20), bg="white", fg='black', command=function2).grid(
    row=4, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating third button
Button(root, text="Recognizer", font=('times new roman', 20), bg="white", fg="black",
       command=function3).grid(row=5, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating attendance button
Button(root, text="Attendance Sheet", font=('times new roman', 20), bg="white", fg="black", command=attend).grid(
    row=6, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)


Button(root, text="Exit", font=('times new roman', 20), bg="red", fg="white", command=function6).grid(row=9,
                            columnspan=2,sticky=N + E + W + S,padx=5, pady=5)

root.mainloop()
