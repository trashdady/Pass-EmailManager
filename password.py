
from tkinter import *
from random import *
from tkinter import messagebox

root=Tk()
entrer = None
root.title('Password Manager')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)



def Enter():
    global entrer
    global entrer2
    global entrer3
    global entrer4
    global entry_password
    username=user.get()
    if not username.isalpha():
        messagebox.showerror("Error","the username can't contain numbers !")
    elif username.isalpha():
        screen=Toplevel(root)
        screen.title("Password Manager")
        img = PhotoImage(file="a.png")
        screen.iconphoto(False,img) 
        screen.geometry('925x500+300+200')

        cr = Label(screen, text="Generate Weak Password :", font=('Arial', 10), padx=5, pady=20)
        cr.grid(row=0, column=4)

        but = Button(screen, text="Generate", command=rand)
        but.grid(row=0, column=6, padx=5, pady=20)

        entrer = Entry(screen, text='', width=40)
        entrer.grid(row=0, column=5, padx=5, pady=20)

        save = Button(screen, text="Save", command=Save)
        save.grid(row=0, column=7, padx=5, pady=20)

        clear = Button(screen, text="Clear", command=Clear)
        clear.grid(row=0, column=8, padx=5, pady=20)

        cr2 = Label(screen, text="Generate Strong Password :", font=('Arial', 10))
        cr2.grid(row=1,column=4, padx=5,pady=20)

        entrer2 = Entry(screen, text='',width=40)
        entrer2.grid(row=1,column=5, padx=5,pady=20)

        but2 = Button(screen, text="Generate", command=rand2)
        but2.grid(row=1,column=6, padx=5,pady=20)

        save2 = Button(screen, text="Save", command=Save2)
        save2.grid(row=1,column=7,padx=5,pady=20)

        clear2 = Button(screen, text="Clear", command=Clear2)
        clear2.grid(row=1,column=8,padx=5,pady=20)

        entrer3 = Entry(screen, text='')
        entrer3.grid(row=2,column=5, padx=5,pady=20)
        but3 = Button(screen, text="Generate", command=rand3)
        but3.grid(row=2,column=6, padx=5,pady=20)
        save3 = Button(screen, text="Save", command=Save3)
        save3.grid(row=2,column=7,padx=5,pady=20)
        clear3 = Button(screen, text="Clear", command=Clear3)
        clear3.grid(row=2,column=8,padx=5,pady=20)
        cr4 = Label(screen, text="Specify Password Length :", font=('Arial', 10))
        cr4.grid(row=2,column=4, padx=5,pady=20)
        entrer4 = Entry(screen, text='')
        entrer4.grid(row=3,column=5, padx=5,pady=20)

        br7 = Label(screen, text="Check Password Strength :", font=('Arial', 10))
        br7.grid(row=4,column=4, padx=5,pady=20)
        entry_password = Entry(screen, text='',width=40)
        entry_password.grid(row=4,column=5, padx=5,pady=20)
        but7 = Button(screen, text="Check", command=rand7)
        but7.grid(row=4,column=6, padx=5,pady=20)
        clear4 = Button(screen, text="Clear", command=Clear4)
        clear4.grid(row=4,column=7,padx=5,pady=20)

def rand():
    password = ''
    for i in range (7):
        password = password + str(randint(1,6))
    entrer.insert(0,password)

def Save():
    password = entrer.get()
    with open("weak_passwords.txt", "a") as f:
        f.write(password)

def Clear():
    entrer.delete(0,END)


def rand2():
    password = ''
    for i in range (13):
        password = password + chr(randint(33,126))
    entrer2.insert(0,password)

def Save2():
    password = entrer2.get()
    with open("strong_passwords.txt", "a") as f:
        f.write(password)

def Clear2():
    try:
        entrer2.delete(0,END)
    except:
        messagebox.showerror("Error","Error404")

def rand2():
    password = ''
    for i in range (13):
        password = password + chr(randint(33,126))
    entrer2.insert(0,password)

def Save2():
    password = entrer2.get()
    with open("strong_passwords.txt", "a") as f:
        f.write(password)

def Clear2():
    try:
        entrer2.delete(0,END)
    except:
        messagebox.showerror("Error","Error404")

def rand3():
    try:
        length = int(entrer3.get())
        password = ''
        for i in range (length):
            password = password + chr(randint(33,126))
        entrer4.insert(0,password)
    except:
        messagebox.showerror("Error","Please write a number")

def Save3():
    try:
        password = entrer4.get()
        with open("Your_passwords.txt", "a") as f:
            f.write(password)
    except:
        messagebox.showerror("Error","Error404")
def Clear3():
    try:
        entrer4.delete(0,END)
    except:
        messagebox.showerror("Error","Error404")

def rand7():
    try:
        entered_password = entry_password.get()
        with open("password.txt", "r") as f:
            for i in f:
                if entered_password == i.strip():
                    messagebox.showwarning("Result", "Password is weak ,choose one from strong password option !")
                    break
            else:
                messagebox.showinfo("Result", "Password is strong.")
    except:
        messagebox.showerror("Error")
def Clear4():
    entry_password.delete(0,END)


        
img = PhotoImage(file="a.png")
root.iconphoto(False,img)

img=PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Please write your username :',fg='black',bg='white',font=('Microsoft YaHei UI Light',10,'bold'))
heading.place(x=22,y=55)


Button(frame,width=39,pady=7,text='Enter',bg='#57a1f8',fg='white',border=0,command=Enter).place(x=35,y=120)
heading=Label(frame,text='Welcome',fg='#58a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

root.mainloop()

