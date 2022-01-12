from tkinter import *
root=Tk()
root.title('201B172')
root.geometry('400x400')
E1=Entry(root,width=16,font="Arial 32")
E1.grid(row=0,column=0,columnspan=4)
B1=Button(root,text="1",width=10,height=5,font="Arial 12")
B1.grid(row=1,column=0)
B2=Button(root,text="2",width=10,height=5,font="Arial 12")
B2.grid(row=1,column=1)
B3=Button(root,text="3",width=10,height=5,font="Arial 12")
B3.grid(row=1,column=2)
B4=Button(root,text="4",width=10,height=5,font="Arial 12")
B4.grid(row=1,column=3)

root.mainloop()
           
