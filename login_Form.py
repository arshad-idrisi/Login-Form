from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Login Form")


def come():
    a = "Arshad"
    b = "Arshad@123"

    if num1.get()== a and num2.get()== b:
        messagebox.showinfo("Hello", "Login Successful!!")
    elif num1.get()!="" and num2.get()!="":
        messagebox.showwarning("Hello", " Wrong username and password!!")
    else:
        messagebox.showerror("Hello", "Empty Login!!")


lbl1 = Label(root, text="UserName : ")
lbl2 = Label(root, text="Password : ")
btn = Button(root, text="Login", command=come)

num1 = Entry(root)
num2 = Entry(root)


lbl1.place(x=90, y=50)
num1.place(x=170, y=50)

lbl2.place(x=90, y=90)
num2.place(x=170, y=90)
btn.place(x=200, y=140)


root.mainloop()