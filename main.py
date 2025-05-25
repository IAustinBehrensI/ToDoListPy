import tkinter as tk
from tkinter import ttk

TaskBtnList = []
DoneBtnList = []

root = tk.Tk()
root.title("To-Do List")

#input
Entry = tk.Entry(root, width = 30,)
Entry.place(x=108,y=40)

LblEntry = tk.Label(root, text = "Please enter your to do list for today", height=1, width=5,bd=1,
                font=("Helvetica", 16, "bold"),fg="white", padx=108, pady=1,   
                 underline=0, wraplength=400)
LblEntry.place(x=115, y=10)

LblToDo = tk.Label(root, text = "To do", bg="black", height=1, width=5,bd=1,
                font=("Helvetica", 16, "bold"),fg="white", padx=30, pady=1,   
                 underline=0, wraplength=250)
LblToDo.place(x=100, y=70)

LblDone = tk.Label(root, text = "Done", bg="black", height=1, width=5,bd=1,                  
                 font=("Helvetica", 16, "bold"),fg="white", padx=30, pady=1,       
                 underline=0, wraplength=250)
LblDone.place(x=290, y=70)

#retrieve text entered and add to list
def GetTask():
   Text = Entry.get()
   Taskbutton = tk.Button(root, text=Text)
   Taskbutton.config (command = lambda b = Taskbutton: CompleteTask(b))
   TaskBtnList.append(Taskbutton)
   RedrawToDoTasks()
   Entry.delete (0,tk.END)
   
def CompleteTask(Taskbutton):
    if Taskbutton in TaskBtnList:
        TaskBtnList.remove(Taskbutton)
        DoneBtnList.append(Taskbutton)
        Taskbutton.config(command=lambda: RemoveDoneTask(Taskbutton))
        RedrawToDoTasks()
        RedrawDoneTasks()

def RemoveDoneTask(Taskbutton):
    if Taskbutton in DoneBtnList:
        DoneBtnList.remove(Taskbutton)
        Taskbutton.destroy()
        RedrawDoneTasks()

def RedrawToDoTasks():
    y=100
    for button in TaskBtnList:
        button.place(x=100,y=y)
        y += 30

def RedrawDoneTasks():
    y=100
    for button in DoneBtnList:
        button.place(x=300,y=y)
        y += 30
def Clear():
    for Cbtn in TaskBtnList:
        Cbtn.destroy()
    for Cbtn in DoneBtnList:
        Cbtn.destroy()
    TaskBtnList.clear()
    DoneBtnList.clear()
    
#add task Button
button = tk.Button (root, text = "Add Task" , command = GetTask)
button.place(x=10, y = 35)

#clear button
Clearbutton = tk.Button(root, text = "Clear", command = Clear)
Clearbutton.place(x=395 , y= 35)

#window size
width = 500
height= 700
root.geometry(f"{width}x{height}")

root.resizable(False, False)

root.bind("<Return>", lambda event: GetTask())

#Run
root.mainloop()
