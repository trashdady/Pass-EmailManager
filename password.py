
from tkinter import *
from random import *
from tkinter import messagebox
from tkinter import ttk
import csv

root=Tk()
entrer = None
root.title('Password and Email Manager')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)





def Enter():
    global wp_ok
    global sp_ok
    global eg_ok

    username=user.get()
    if not username.isalpha():
        messagebox.showerror("Error","the username can't contain numbers !")
    elif username.isalpha():
        screen=Toplevel(root)
        screen.title("Password and Email Manager")
        img = PhotoImage(file="a.png")
        screen.iconphoto(False,img) 
        screen.geometry('560x150')




        wp = Label(screen, text="Generate Weak Password :", font=('Arial', 10))
        wp.grid(row=0,column=0,padx=5,pady=5)
        wp_ok = Entry(screen, text='',width=35)
        wp_ok.grid(row=0,column=1)
        gen_wp = Button(screen, text="Generate", command=rand)
        gen_wp.grid(row=0,column=2,padx=10,pady=5)
        save_wp = Button(screen, text="Save", command=Save)
        save_wp.grid(row=0,column=3,padx=0,pady=5)
        clear_wp = Button(screen, text="Clear", command=Clear)
        clear_wp.grid(row=0,column=4,padx=5,pady=5)

        sp = Label(screen, text="Generate Strong Password :", font=('Arial', 10))
        sp.grid(row=1,column=0, padx=5,pady=5)
        sp_ok = Entry(screen, text='',width=35)
        sp_ok.grid(row=1,column=1)
        gen_sp = Button(screen, text="Generate", command=rand2)
        gen_sp.grid(row=1,column=2, padx=0,pady=5)
        save_sp = Button(screen, text="Save", command=Save2)
        save_sp.grid(row=1,column=3,padx=0,pady=5)
        clear_sp = Button(screen, text="Clear", command=Clear2)
        clear_sp.grid(row=1,column=4,padx=5,pady=5)

        eg=Label(screen,text="Generate Email :",font=('Arial', 10))
        eg.grid(row=2,column=0,padx=5,pady=5)
        eg_ok = Entry(screen,text="",width=35)
        eg_ok.grid(row=2,column=1)
        eg_button=Button(screen, text="Generate",command=generate_email)
        eg_button.grid(row=2,column=2)
        save_eg = Button(screen, text="Save", command=Save3)
        save_eg.grid(row=2,column=3,padx=0,pady=5)
        clear_eg = Button(screen, text="Clear", command=Clear3)
        clear_eg.grid(row=2,column=4,padx=5,pady=5)

        save_data=Button(screen, text = "Next" ,command=Data)
        save_data.grid(row=3,column=1)
        

        





def rand():
    password = ''
    for i in range (7):
        password = password + str(randint(1,6))
    wp_ok.insert(0,password)

def Save():
    password = wp_ok.get()
    with open("weak_passwords.txt", "a") as f:
        f.write(password)

def Clear():
    wp_ok.delete(0,END)

def rand2():
    password = ''
    for i in range (13):
        password = password + chr(randint(33,126))
    sp_ok.insert(0,password)

def Save2():
    password = sp_ok.get()
    with open("strong_passwords.txt", "a") as f:
        f.write(password)

def Clear2():
    try:
        sp_ok.delete(0,END)
    except:
        messagebox.showerror("Error","Error404")

def generate_email():
    f_name = ["Ali","Mustapha","Amine","Oussama"]
    l_name = ["Ouachou","Salimi","Katiri","Youssefi"]

    rand_num = randint(20,99)
    x=choice(f_name)
    y=choice(l_name)
    rand_email=f"{x.lower()}{y.lower()}{rand_num}@gmail.com"
    eg_ok.insert(0,rand_email)
      

def Save3():
    password = eg_ok.get()
    with open("email.txt", "a") as f:
        f.write(password)
    
def Clear3():
    try:
        eg_ok.delete(0,END)
    except:
        messagebox.showerror("Error","Error404")

def Data():
    w =  sp_ok.get()
    i = eg_ok.get()
    y = f"Your Email : {i} \n Your Password : {w}"
    messagebox.showinfo("Data",y)


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

