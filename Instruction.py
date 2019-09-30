from Tkinter import *
y=Tk()
y.title("Instruction")
 
def ins():
    y.destroy()

nb=Label(y,compound='center',text='Please Install Pygame Module \n If You want to run this program\n other than Network Drive then\n please select path and change it inside the source Code',bg='blue',font=" times 30 bold italic",fg='white')

nb.after(7000,ins)
nb.pack()
y.mainloop()
