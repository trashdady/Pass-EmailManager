from tkinter import *
from random import *
from tkinter import messagebox
import csv

apk = Tk()

apk.title("Password Manager")

img = PhotoImage(file="a.png")
apk.iconphoto(False,img) 

background_image = PhotoImage(file="e.png")

background_label = Label(apk, image=background_image)
background_label.place(relwidth=1, relheight=1)

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

def Data():
    w =  web_entry.get()
    u = user_entry.get()
    i = id_entry.get()
    p = ps_entry.get()
    y = ["Website Or App Name :",w,"Username :",u,"ID :",i,"Password :",p]
    x= ["Website","Username","ID","Password"]
    z= [w , u , i , p]
    data.insert(0,y)
    with open("data.csv","a") as f:
        writer = csv.writer(f,delimiter=";")
        writer.writerow(x)
        writer.writerow(z)

def ClearD():
    data.delete(0,END)
    
cr = Label(apk, text="Generate Weak Password :", font=('Arial', 10),bg="white")
but = Button(apk, text="Generate", command=rand)
entrer = Entry(apk, text='',width=40)
save = Button(apk, text="Save", command=Save)
clear = Button(apk, text="Clear", command=Clear)
web = Label(apk, text="Website Or App Name :", font=('Arial', 10),bg="white")
web_entry = Entry(apk, text='',width=40)
user = Label(apk, text="Username :", font=('Arial', 10),bg="white")
user_entry = Entry(apk, text='',width=40)
id = Label(apk, text="ID :", font=('Arial', 10),bg="white")
id_entry = Entry(apk, text='',width=40)
ps = Label(apk, text="Password :", font=('Arial', 10),bg="white")
ps_entry = Entry(apk, text='',width=40)
data_label = Label(apk, text="DATA :", font=('Arial', 10),bg="white")
data = Entry(apk,width=105)
Save9 = Button(apk, text="Save Data", command=Data)
clear9 = Button(apk, text="clear",command=ClearD)

cr.grid(row=0,column=4,padx=5,pady=20)
but.grid(row=0,column=6,padx=5,pady=20)
entrer.grid(row=0,column=5,padx=5,pady=20)
save.grid(row=0,column=7,padx=5,pady=20)
clear.grid(row=0,column=8,padx=5,pady=20)
web_entry.grid(row=0,column=1,padx=5,pady=20)
web.grid(row=0,column=0,padx=5,pady=20)
user.grid(row=1,column=0,padx=5,pady=20)
user_entry.grid(row=1,column=1,padx=5,pady=20)
id.grid(row=2,column=0,padx=5,pady=20)
id_entry.grid(row=2,column=1,padx=5,pady=20)
ps.grid(row=3,column=0,padx=5,pady=20)
ps_entry.grid(row=3,column=1,padx=5,pady=20)
data.grid(row=5,column=1,padx=5,pady=20)
data_label.grid(row=5,column=0,padx=5,pady=40)
Save9.grid(row=5,column=4)
clear9.grid(row=5,column=5)

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

cr2 = Label(apk, text="Generate Strong Password :", font=('Arial', 10),bg="white")
entrer2 = Entry(apk, text='',width=40)
but2 = Button(apk, text="Generate", command=rand2)
save2 = Button(apk, text="Save", command=Save2)
clear2 = Button(apk, text="Clear", command=Clear2)

cr2.grid(row=1,column=4, padx=5,pady=20)
but2.grid(row=1,column=6, padx=5,pady=20)
entrer2.grid(row=1,column=5, padx=5,pady=20)
save2.grid(row=1,column=7,padx=5,pady=20)
clear2.grid(row=1,column=8,padx=5,pady=20)

def rand3():
    try:
        length = int(entrer3.get())
        password = ''
        for i in range (length):
            password = password + chr(randint(33,126))
        entrer4.insert(0,password)
    except:
        messagebox.showerror("Error","Error404")

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

cr4 = Label(apk, text="Specify Password Length :", font=('Arial', 10),bg="white")
entrer3 = Entry(apk, text='')
but3 = Button(apk, text="Generate", command=rand3)
entrer4 = Entry(apk, text='')
save3 = Button(apk, text="Save", command=Save3)
clear3 = Button(apk, text="Clear", command=Clear3)

cr4.grid(row=2,column=4, padx=5,pady=20)
but3.grid(row=2,column=6, padx=5,pady=20)
entrer3.grid(row=2,column=5, padx=5,pady=20)
entrer4.grid(row=3,column=5, padx=5,pady=20)
save3.grid(row=2,column=7,padx=5,pady=20)
clear3.grid(row=2,column=8,padx=5,pady=20)

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

br7 = Label(apk, text="Check Password Strength :", font=('Arial', 10))
entry_password = Entry(apk, text='',width=40)
but7 = Button(apk, text="Check", command=rand7)
clear4 = Button(apk, text="Clear", command=Clear4)

br7.grid(row=4,column=4, padx=5,pady=20)
entry_password.grid(row=4,column=5, padx=5,pady=20)
but7.grid(row=4,column=6, padx=5,pady=20)
clear4.grid(row=4,column=7,padx=5,pady=20)

apk.resizable(width=False,height=False)

apk.mainloop()
