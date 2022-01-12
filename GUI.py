from tkinter import *
root=Tk()
root.title('GUI_201B172')
root.geometry('400x400')
Label(root,text="Enter YOur Age : ").grid(row=0,column=0)
def fun():
    #Label(root,text="Welcome to Juet Guna M.P.").pack()
    age=E1.get()#after getting the value we are using it .
    if int(age)>=18:
        msg=' ADULT'
    else:
        msg=' Minor'
    La1=Label(root,text="Message : You Are"+msg) # we can use above line like this also
    La1.grid(row=2,column=0)

#Button(root,text="Submit").pack()
#B1=Button(root,text="Submit",command=root.bell) # we can use above line like this also
E1=Entry(root)
E1.grid(row=0,column=1)
B1=Button(root,text="Submit",command=fun)# function is called here without brackets
B1.grid(row=1,column=1)



root.mainloop()
