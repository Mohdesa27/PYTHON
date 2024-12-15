from tkinter  import * 
x=Tk()
x.geometry("400*400")
l=Label(text="name")
l.grid(row=0,column=0)#l.pack
e=Entry()
e.grid(row=0,column=1)
b=Button()
b.grid(row=1,column=1)
x.mainloop()