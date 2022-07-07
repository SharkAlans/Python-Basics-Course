
from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.title('GUI-Calculator')
GUI.geometry('700x600')

# bg = PhotoImage(file='car.png')

# BG = Label(GUI, image=bg)
# BG.pack()

L = Label(GUI,text='Fish quantity (100 grams)',font=(None,20))
L.pack()

v_quantity = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()

def Cal():
    try:    
        quan = float(v_quantity.get())
        calc = quan * 1
        v_quantity.set('')
        messagebox.showinfo('Total Price','Total Fish Price {} $'.format(calc) )
    except:
        messagebox.showinfo('Error, you have enter somethong invalid. Please use only numbers')
        v_quantity.set('')
B = ttk.Button(GUI, text='Calculate',command=Cal)
B.pack(ipadx=30,ipady=20,pady=20)

GUI.mainloop()