import tkinter
from tkinter import*


root=tkinter.Tk()
root.title('demo')
root.geometry('600x600')
#label=tkinter.Label(root,text='select a programming language').pack()#label
#button
b=Button(root,text='subscribe',bg='red',fg='white')
b.grid(column=1,row=0)
r=Radiobutton(root,text='java',value=1)
r.grid(column=2,row=1)
r1=Radiobutton(root,text='python',value=2)
r1.grid(column=3,row=1)
r2=Radiobutton(root,text='Html',value=3)
r2.grid(column=4,row=1)
r3=Radiobutton(root,text='c++',value=4)
r3.grid(column=5,row=1)
e=Entry(root,width=25)#entry
e.grid(column=1,row=2)
root.mainloop()

