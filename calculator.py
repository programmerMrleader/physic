from tkinter import *

def button_click(number):
	current = entry.get()
	entry.delete(0,END)
	entry.insert(0,str(current)+str(number))
def button_add():
	first_number = entry.get()
	global f_num
	f_num = int(first_number)
	entry.delete(0,END)
	
def clear():
	entry.delete(0,END)

def button_equal():
	second_number = entry.get()
	entry.delete(0,END)
	entry.insert(0, f_num + int(second_number))
root = Tk()

entry = Entry(root,width=35,borderwidth=19)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

button_1 = Button(root,text=1,width=10,height=5,command=lambda: button_click(1))
button_1.grid(row=3,column=0)

button_2 = Button(root,text=2,width=10,height=5,command=lambda: button_click(2))
button_2.grid(row=3,column=1)

button_3 = Button(root,text=3,width=10,height=5,command=lambda: button_click(3))
button_3.grid(row=3,column=2)

button_4 = Button(root,text=4,width=10,height=5,command=lambda: button_click(4))
button_4.grid(row=2,column=0)

button_5 = Button(root,text=5,width=10,height=5,command=lambda: button_click(5))
button_5.grid(row=2,column=1)

button_6 = Button(root,text=6,width=10,height=5,command=lambda: button_click(6))
button_6.grid(row=2,column=2)

button_7 = Button(root,text=7,width=10,height=5,command=lambda: button_click(7))
button_7.grid(row=1,column=0)

button_8 = Button(root,text=8,width=10,height=5,command=lambda: button_click(8))
button_8.grid(row=1,column=1)

button_9 = Button(root,text=9,width=10,height=5,command=lambda: button_click(9))
button_9.grid(row=1,column=2)

button_0 = Button(root,text=0,width=10,height=5,command=lambda: button_click(0))
button_0.grid(row=4,column=0)

button_clear = Button(root,text="Clear",height=5,width=22,command=clear)
button_clear.grid(row=4,column=1,columnspan=2)

button_add = Button(root,text="+",height=5,width=10,command=button_add)
button_add.grid(row=5,column=0)

button_equal = Button(root,text="=",height=5,width=22,command=button_equal)
button_equal.grid(row=5,column=1,columnspan=2)

root.mainloop()