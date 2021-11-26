from tkinter import *

root = Tk()
root.resizable(False,False)
root.title("To-Do List")


mainFrame = Frame(root)
mainFrame.config(width = 400, height = 300)
mainFrame.pack()

task = StringVar()

Label(mainFrame, text = "To-Do List").place(relx = 0.1, rely = 0.1)
Label(mainFrame, text = "Enter new Task: ").place(relx = 0.1, rely = 0.25)

Entry(mainFrame, textvariable = task, width = 25, borderwidth = 2).place(relx = 0.1, rely = 0.35)

Button(mainFrame, text = "Add task", width = 20).place(relx = 0.1, rely = 0.45)
Button(mainFrame, text = "Delete", width = 20).place(relx = 0.1, rely = 0.55)
Button(mainFrame, text = "Delete All", width = 20).place(relx = 0.1, rely = 0.65)
Button(mainFrame, text = "Exit", width = 20).place(relx = 0.1, rely = 0.75)

Listbox(mainFrame, width = 25, height = 12).place(relx = 0.55, rely = 0.25)


root.mainloop()