from Tkinter import *
x=Tk()
x.title("AboutUs")
dp=PhotoImage(file="splash.gif")
 
def des():
    x.destroy()

lb=Label(x,image=dp,compound='center',text='Name:- Divyam Saxena\n Enrollment NO.:-161B076\nBatch:-BX(B3)\nTitle:-Music Player',bg='blue',font=" times 30 bold italic",fg='white')

lb.after(2500,des)
lb.pack()
x.mainloop()
