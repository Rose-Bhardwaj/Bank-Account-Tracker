#__________________SOURCE CODE OF OUR PROJECT - BANK MANAGEMENT__________________

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import mysql.connector as mc
import datetime as dt
import csv
#---------------------------------------------------------------------------------

#function to exit current frame

def back(frame):
            frame.destroy()

#function to exit current fwindow
def close(window):
        window.withdraw()  

#function to change colour of button upon hovering
def changeOnHover(button,bge,bgl):
    button.bind("<Enter>", func=lambda e: button.config(bg=bge))
    button.bind("<Leave>", func=lambda e: button.config(bg=bgl))
    
#function to validate date
def date(date_str):
    try:
        return bool(dt.datetime.strptime(date_str, '%Y-%m-%d'))
    except ValueError:
        return False
    
#function to get values from Personal table based on User_ID
def find_user(X):
    V = (X,)
    Q = "select * from Personal where User_ID = %s"
    cur.execute(Q,V)
    res = cur.fetchone()
    if res == None:
        return False

#function to get values from Personal table based on Name  
def find_name(X):
    V = (X,)
    Q = "select * from Personal where Name = %s"
    cur.execute(Q,V)
    res = cur.fetchone()
    if res != None:
        return True

#function to get values from Account table based on Acc_Num    
def find_acct(X):
    V = (X,)
    Q = "select * from Account where Acc_Num = %s"
    cur.execute(Q,V)
    res = cur.fetchone()
    if res == None:
        return False

#function to fetch the current deposit amount of user
def get_bal_amt(X):
    V = (X,)
    Q = "select deposit from Account where Acc_num=%s"
    cur.execute(Q,V)
    res = cur.fetchone()
    return str(res[0])

#function to assign User_ID to a new user
def set_user_id(name):
    user_id = ''
    n = name.split()
    initials = ''
    for i in n:
        initials += i[0].upper()
    q = "select count(*) from Personal"
    cur.execute(q)
    res = cur.fetchone()
    user_id = str(res[0]+1)+'-'+initials
    return user_id

#function to assign Acc_Num to a new account
def set_acc_num():
    acc_num = ''
    q = "select max(Acc_Num) from Account"
    cur.execute(q)
    res = cur.fetchone()
    if res[0] == None:
        acc_num='001'
    else:
        x = int(res[0]) + 1
        if x<10:
            acc_num = '00' + str(x)
        if x>=10 and x<100:
            acc_num = '0' + str(x)
        if x>=100:
            acc_num = str(x)
    return acc_num
#---------------------------------------------------------------------------------

#function to enter new account page
def new_act(menu):
    f1=Frame(menu,width=685,height=400,bg='black')
    f1.place(x=400,y=115)

    h = Label(f1,text='Open A New Account',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',18,'bold'))
    h.place(x=200, y=50)
    Frame(f1,width=300,height=1,bg='white').place(x=185,y=90)
    btn1=Button(f1,width=15,padx=30,pady=5,text='Profile',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(f1),profile(menu)])
    btn1.place(x=235,y=120)
    changeOnHover(btn1, "gainsboro","white")
    btn2=Button(f1,width=15,padx=30,pady=5,text='Account',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(f1),acct(menu)])
    btn2.place(x=235,y=170)
    changeOnHover(btn2, "gainsboro","white")
    btn=Button(f1,width=8,padx=20,pady=5,text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12),command=lambda: back(f1))
    btn.place(x=280,y=240)
    changeOnHover(btn, "gainsboro","white")
#---------------------------------------------------------------------------------
    
#function to create a profile 
def profile(menu):
    f1a=Frame(menu,width=685,height=400,bg='black')
    f1a.place(x=400,y=115)
    h1 = Label(f1a,text='Profile',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',18,'bold'))
    h1.place(x=295, y=10)
    h2 = Label(f1a,text='Enter your personal details...',fg='white',bg='black',font=('Microsoft YaHei UI Light',10))
    h2.place(x=250,y=40)
    l1 = Label(f1a,text='Name: ',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))
    e1 = Entry(f1a,width=25,fg='white',bg='black',border=0,font=('Microsoft YaHei UI Light',11))
    l1.place(x=180,y=80)
    e1.place(x=320,y=80)
    Frame(f1a,width=200,height=1,bg='white').place(x=320,y=100)
    l2 = Label(f1a,text='Age: ',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))
    e2 = Entry(f1a,width=25,fg='white',bg='black',border=0,font=('Microsoft YaHei UI Light',11))
    l2.place(x=180,y=137)
    e2.place(x=320,y=140)
    Frame(f1a,width=200,height=1,bg='white').place(x=320,y=160)
    l3= Label(f1a,text='Date Of Birth: ',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))
    l3a = Label(f1a,text='(YYYY-MM-DD)',fg='white',bg='black',font=('Microsoft YaHei UI Light',10))
    e3 = Entry(f1a,width=25,fg='white',bg='black',border=0,font=('Microsoft YaHei UI Light',11))
    l3.place(x=180,y=200)
    l3a.place(x=180,y=220)
    e3.place(x=320,y=200)
    Frame(f1a,width=200,height=1,bg='white').place(x=320,y=220)
    l4= Label(f1a,text='Address: ',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))
    l4a = Label(f1a,text='(name of city/town)',fg='white',bg='black',font=('Microsoft YaHei UI Light',10))
    e4 = Entry(f1a,width=25,fg='white',bg='black',border=0,font=('Microsoft YaHei UI Light',11))
    l4.place(x=180,y=260)
    l4a.place(x=180,y=280)
    e4.place(x=320,y=260)
    Frame(f1a,width=200,height=1,bg='white').place(x=320,y=280)
    l5= Label(f1a,text='Salary: ',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))
    e5 = Entry(f1a,width=25,fg='white',bg='black',border=0,font=('Microsoft YaHei UI Light',11))
    l5.place(x=180,y=320)
    e5.place(x=320,y=320)
    Frame(f1a,width=200,height=1,bg='white').place(x=320,y=340)
    
    back_btn=Button(f1a,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f1a))
    back_btn.place(x=180,y=358)
    changeOnHover(back_btn, "gainsboro","white")
    go_btn=Button(f1a,width=15, text='Go to Accounts',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: [back(f1a),acct(menu)])
    go_btn.place(x=390,y=358)
    changeOnHover(go_btn, "gainsboro","white")
    enter_btn=Button(f1a,width=10, text='Enter',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10, 'bold'),command=lambda: enter_profile([e1.get(),e2.get(),e3.get(),e4.get(),e5.get()]))
    enter_btn.place(x=270,y=358)
    changeOnHover(enter_btn, "gainsboro","white")
    
#function to create a profile (adding values to table Personal)    
def enter_profile(L):
    date_format = '%y-%m-%d'
    val = True
    
    if (L[0]=='') or (L[1]=='')or (L[2]=='') or (L[3]=='') or (L[4]==''):
        mb.showerror('Empty fields','Please fill all details!')
        val = False
        
    bool = find_name(L[0])
    if bool == True:
        mb.showerror('Duplicate','The entered User-ID already exists!')
        mb.showinfo('','Click Go To Accounts if you want to create another account.')
        val = False
        
    for i in L[0]:
        if i != ' ':
            if i.isalpha() == False:
                mb.showerror('Invalid','Only alphabets permitted for name field!')
                val = False
                break
            
    for i in L[1]:
        if i.isdigit() == False:
            mb.showerror('Invalid','Only integers permitted for age field!')
            val = False
            break
        
    if L[2]!='':
        if len(L[2]) != 10:
            mb.showerror('Invalid','Enter date in format YYYY-MM-DD!')
            val = False
        else:  
            bool = date(L[2])
            if bool == False:
                mb.showerror('Invalid','Enter a valid date!')
                val = False
        
        '''if len(L[2]) != 10:
            mb.showerror('Invalid','Enter date in format YYYY-MM-DD!')
            val = False
        else:
            mon = int(L[2][5:7])
            day = int(L[2][8:10])
            if mon>12:
                mb.showerror('Invalid','Enter valid month!')
                val = False
            if day>31:
                mb.showerror('Invalid','Enter valid day!')
                
                val = False'''
    for i in L[3]:
        if i != ' ':
            if i.isalpha() == False:
                mb.showerror('Invalid','Only alphabets permitted for address field!')
                val = False
                break
            
    for i in L[4]:
        if i.isdigit() == False:
            mb.showerror('Invalid','Only integers permitted for salary field!')
            val = False
            break
        
    if val == True:
        x = set_user_id(L[0])
        vals =(x,L[0],int(L[1]),L[2],L[3],int(L[4]))
        q="insert into Personal values(%s,%s,%s,%s,%s,%s)"
        cur.execute(q,vals)
        con.commit()
        mb.showinfo('Saved',"Your personal details have been saved!")
        mb.showinfo('Note',("Your User ID is:  ",x))
#---------------------------------------------------------------------------------
        
#function to create an account     
def acct(menu):
    f1b=Frame(menu,width=685,height=400,bg='black')
    f1b.place(x=400,y=115)

    h1 = Label(f1b,text='Fresh Account',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',18,'bold'))
    h1.place(x=265, y=15)
    h2 = Label(f1b,text='Enter account details for your new account...',fg='white',bg='black',font=('Microsoft YaHei UI Light',10))
    h2.place(x=220, y=50)

    l1= Label(f1b,text='User ID: ',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))
    e1 = Entry(f1b,width=25,fg='white',bg='black',border=0,font=('Microsoft YaHei UI Light',11))
    l1.place(x=160,y=100)
    e1.place(x=340,y=100)
    Frame(f1b,width=200,height=1,bg='white').place(x=340,y=130)
    
    l2a = Label(f1b,text='(any valid date)',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))            
    e2 = Entry(f1b,width=25,fg='white',bg='black',border=0,font=('Microsoft YaHei UI Light',11))
    l2.place(x=160,y=160)
    l2a.place(x=160,y=183)
    e2.place(x=340,y=160)
    Frame(f1b,width=200,height=1,bg='white').place(x=340,y=180)

    l3= Label(f1b,text='Starting deposit: ',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))
    e3 = Entry(f1b,width=25,fg='white',bg='black',border=0,font=('Microsoft YaHei UI Light',11))
    l3.place(x=160,y=220)
    e3.place(x=340,y=220)
    Frame(f1b,width=200,height=1,bg='white').place(x=340,y=240)

    l4= Label(f1b,text='Account Description: ',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))
    l4a = Label(f1b,text='(savings/loan/insurance)',fg='white',bg='black',font=('Microsoft YaHei UI Light',11))
    '''menu= StringVar()
    menu.set("          Select          ")

    drop = OptionMenu(f1b, menu,"Savings", "Loan","Insurance")
    drop.place(x=320,y=300)'''

    e4 = Entry(f1b,width=25,fg='white',bg='black',border=0,font=('Microsoft YaHei UI Light',11))
    l4.place(x=160,y=280)
    l4a.place(x=160,y=300)
    e4.place(x=340,y=280)
    Frame(f1b,width=200,height=1,bg='white').place(x=340,y=300)

    back_btn=Button(f1b,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f1b))
    back_btn.place(x=160,y=345)
    changeOnHover(back_btn, "gainsboro","white")

    go_btn=Button(f1b,width=15, text='Go to Profile',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: [back(f1b),profile(menu)])
    go_btn.place(x=410,y=345)
    changeOnHover(go_btn, "gainsboro","white")

    enter_btn=Button(f1b,width=10, text='Enter',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10, 'bold'),command=lambda: enter_acct([e1.get(),e2.get(),e3.get(),e4.get()]))
    enter_btn.place(x=270,y=345)
    changeOnHover(enter_btn, "gainsboro","white")

#function to create new Account (adding values to table Account)
def enter_acct(L):
    val = True
    
    if (L[0]=='') or (L[1]=='') or (L[2]=='') or (L[3]==''):
        mb.showerror('Empty fields','Please fill all details!')
        val = False
        
    bool = find_user(L[0])
    if bool == False:
        mb.showerror('Not found','The entered User-ID doesnt exist!')
        val = False
        
    if L[1]!='':
        if len(L[1]) != 10:
            mb.showerror('Invalid','Enter date in format YYYY-MM-DD!')
            val = False
        else:  
            bool = date(L[1])
            if bool == False:
                mb.showerror('Invalid','Enter a valid date!')
                val = False
                
    for i in L[2]:
        if i.isdigit() == False:
            mb.showerror('Invalid','Only integers permitted for deposit field!')
            val = False
            break
        
    for i in L[3]:
        if i != ' ':            
            if i.isalpha() == False:
                mb.showerror('Invalid','Only alphabets permitted for description field!')
                val = False
                break
            
    if L[3].lower() not in ['savings','loan','insurance']:
        mb.showerror('Invalid','You can only make account for the following purposes:\n1. savings\n2. loan\n3. insurance')
        val = False
        
    q1 = 'select count(Acc_num) from Account where User_ID = %s'
    v = (L[0],)
    cur.execute(q1,v)
    res = cur.fetchone()
    #print(res)
    if res[0] >= 1:
        q2 = 'select Acc_Desc from Account where User_ID = %s'
        cur.execute(q2,v)
        res = cur.fetchall()
        #print(res) #[('savings'),('loan')]
        for i in res:
            #print(i)
            if L[3] in i:
                mb.showerror('Invalid','You already have an account under for the same purpose!')
                val = False
                break

    if val == True:
        x = set_acc_num()
        vals =(x,L[1],int(L[2]),L[3],L[0])
        q="insert into Account values(%s,%s,%s,%s,%s)"
        cur.execute(q,vals)
        con.commit()
        mb.showinfo('Saved',"Your account details have been saved!")
        mb.showinfo('Note',("Your account number is:  ",x))
#---------------------------------------------------------------------------------

#function to view account/all accounts 
def vw_acct(menu):
    f2=Frame(menu,width=685,height=400,bg='black')
    f2.place(x=400,y=115)               

    #function to view single account
    def  nxt1():
        f2a=Frame(f2,width=685,height=300,bg='black')
        f2a.place(x=0,y=240)
        l = Label(f2a,text='Enter your User-ID: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))#specify wch column
        l.place(x=130,y=0)
        e = Entry(f2a,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
        e.place(x=320,y=0)
        b = Button(f2a,padx=10,text='View',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: [vw_one_acct(menu,e.get()),back(f2),])
        b.place(x=300,y=40)
        changeOnHover(b, "gainsboro","white")
        back_btn=Button(f2a,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f2a))
        back_btn.place(x=290,y=85)
        changeOnHover(back_btn, "gainsboro","white")
                  

    h1 = Label(f2,text='View Account',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',18,'bold'))
    h1.place(x=260, y=50)
    Frame(f2,width=300,height=1,bg='white').place(x=195,y=90)
    
    b1=Button(f2,width=25,pady=5,text='View all accounts',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(f2),vw_all_accts(menu)])
    b1.place(x=210,y=120)
    changeOnHover(b1, "gainsboro","white")
    
    b2=Button(f2,width=25,pady=5,text='View my account',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: nxt1())
    b2.place(x=210,y=170)
    changeOnHover(b2, "gainsboro","white")
    
    back_btn=Button(f2,width=8,padx=20,pady=5,text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12),command=lambda:back(f2))
    back_btn.place(x=290,y=240)
    changeOnHover(back_btn, "gainsboro","white")

#function to view all accounts
def vw_all_accts(menu):  
    q = "select * from Personal NATURAL JOIN Account;"
    cur.execute(q)
    res = cur.fetchall()

    f = Frame(menu,width=685,height=400,bg='black')
    f.place(x=400,y=115)
    
    back_btn=Button(f,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f))
    back_btn.place(x=300,y=350)
    changeOnHover(back_btn, "gainsboro","white")

    treef = Frame(f,width=685,height=300,bg='black')
    treef.place(x=0,y=0)

    tree = ttk.Treeview(treef)
    tree.place(x=0,y=0)
    tree.pack(expand=True,fill=BOTH)

    tree['columns']=('User_ID','Name','Age','DOB','Address','Salary','Acc_Num','Open_date','deposit','Acc_Desc')
    tree.column('#0',width=0,stretch=NO)
    tree.column('User_ID',anchor=W,width=52)
    tree.column('Name',anchor=W,width=110)
    tree.column('Age',anchor=W,width=35)
    tree.column('DOB',anchor=W,width=80)
    tree.column('Address',anchor=W,width=70)
    tree.column('Salary',anchor=W,width=55)
    tree.column('Acc_Num',anchor=W,width=62)
    tree.column('Open_date',anchor=W,width=80)
    tree.column('deposit',anchor=W,width=60)
    tree.column('Acc_Desc',anchor=W,width=80)
    
    tree.heading('#0',text='')
    tree.heading('User_ID',text='User_ID',anchor=W)
    tree.heading('Name',text='Name',anchor=W)
    tree.heading('Age',text='Age',anchor=W)
    tree.heading('DOB',text='DOB',anchor=W)
    tree.heading('Address',text='Address',anchor=W)
    tree.heading('Salary',text='Salary',anchor=W)
    tree.heading('Acc_Num',text='Acc_Num',anchor=W)
    tree.heading('Open_date',text='Open_date',anchor=W)
    tree.heading('deposit',text='deposit',anchor=W)
    tree.heading('Acc_Desc',text='Acc_Desc',anchor=W)
    
    for i in range(len(res)):
        tree.insert(parent='',index='end',iid=i,text='',values=(res[i][0],res[i][1],res[i][2],res[i][3],res[i][4],res[i][5],res[i][6],res[i][7],res[i][8],res[i][9]))
        tree.pack(expand=True,fill=BOTH)

#function to view an account based on User_ID
def vw_one_acct(menu,x):
    bool = find_user(x)
    if bool == False:
        mb.showerror('Not found','The entered User-ID doesnt exist!')
    else:
        q = "select * from Personal NATURAL JOIN Account where User_ID =%s;"
        v = (x,)
        cur.execute(q,v)
        res = cur.fetchall()

        f = Frame(menu,width=685,height=400,bg='black')
        f.place(x=400,y=115)
        
        back_btn=Button(f,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f))
        back_btn.place(x=300,y=350)
        changeOnHover(back_btn, "gainsboro","white")

        treef = Frame(f,width=685,height=300,bg='black')
        treef.place(x=0,y=0)

        tree = ttk.Treeview(treef)
        tree.place(x=0,y=0)
        tree.pack(expand=True,fill=BOTH)

        tree['columns']=('User_ID','Name','Age','DOB','Address','Salary','Acc_Num','Open_date','deposit','Acc_Desc')
        tree.column('#0',width=0,stretch=NO)
        tree.column('User_ID',anchor=W,width=52)
        tree.column('Name',anchor=W,width=110)
        tree.column('Age',anchor=W,width=35)
        tree.column('DOB',anchor=W,width=80)
        tree.column('Address',anchor=W,width=70)
        tree.column('Salary',anchor=W,width=55)
        tree.column('Acc_Num',anchor=W,width=62)
        tree.column('Open_date',anchor=W,width=80)
        tree.column('deposit',anchor=W,width=60)
        tree.column('Acc_Desc',anchor=W,width=80)
        
        tree.heading('#0',text='')
        tree.heading('User_ID',text='User_ID',anchor=W)
        tree.heading('Name',text='Name',anchor=W)
        tree.heading('Age',text='Age',anchor=W)
        tree.heading('DOB',text='DOB',anchor=W)
        tree.heading('Address',text='Address',anchor=W)
        tree.heading('Salary',text='Salary',anchor=W)
        tree.heading('Acc_Num',text='Acc_Num',anchor=W)
        tree.heading('Open_date',text='Open_date',anchor=W)
        tree.heading('deposit',text='deposit',anchor=W)
        tree.heading('Acc_Desc',text='Acc_Desc',anchor=W)

        for i in range(len(res)):
            tree.insert(parent='',index='end', iid=i,text='',values=(res[i][0],res[i][1],res[i][2],res[i][3],res[i][4],res[i][5],res[i][6],res[i][7],res[i][8],res[i][9]))
            tree.pack(expand=True,fill=BOTH)
#---------------------------------------------------------------------------------

#function to modify account details
def mod_act(menu):
    f3=Frame(menu,width=685,height=400,bg='black')
    f3.place(x=400,y=115)                   

    #function to recieve details
    def  nxt2():
        f3a=Frame(f3,width=685,height=195,bg='black')
        f3a.place(x=120,y=280)
        
        l3 = Label(f3a,text='Enter new info: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
        l3.place(x=170,y=0)
        e2 = Entry(f3a,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
        e2.place(x=135,y=30)
        
        b2 = Button(f3a,padx=10,text='Modify',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda:modify(e.get(),e1.get(),e2.get()))
        b2.place(x=135,y=70)
        changeOnHover(b2, "gainsboro","white")
        
        back_btn = Button(f3a,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f3a))
        back_btn.place(x=245,y=70)
        changeOnHover(back_btn, "gainsboro","white")
    
    h1 = Label(f3,text='Modifying Account',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',18,'bold'))
    h1.place(x=230,y=20)
    Frame(f3,width=300,height=1,bg='white').place(x=185,y=60)
    
    l = Label(f3,text='Enter User-ID: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
    l.place(x=170,y=90)
    
    e = Entry(f3,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
    e.place(x=330,y=90)
    l1 = Label(f3,text='What do you want to modify: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
    l1.place(x=230,y=140)
    
    l2 = Label(f3,text='Name/Age/DOB/Address/Salary: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',8))
    l2.place(x=255,y=165)
    e1 = Entry(f3,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
    e1.place(x=255,y=200)
    
    b1 = Button(f3,padx=10,text='Next',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda:nxt2())
    b1.place(x=255,y=240)
    changeOnHover(b1, "gainsboro","white")
    
    back_btn = Button(f3,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f3))
    back_btn.place(x=365,y=240)
    changeOnHover(back_btn, "gainsboro","white")


#function to modify personal details based on User_ID
def modify(x,coln,newval):
    bool = find_user(x)
    val = True
    
    if x=='' or coln=='' or newval=='' :
        mb.showerror('Empty fields','Please fill all details!')
        val = False
    else:
        if bool == False:
            mb.showerror('Not found','The entered User-ID doesnt exist!')
            val = False
            
        if coln not in ['Name','Age','DOB','Address','Salary']:
            mb.showerror('','Enter valid column name to modify!')
            val = False

        if coln == 'Name':
            for i in newval:
                if i != ' ':
                    if i.isalpha() == False:
                        mb.showerror('Invalid','Only alphabets permitted for name field!')
                        val = False
                        break            

        if coln == 'Age':
                if newval.isdigit() == False:
                    mb.showerror('Invalid','Only integers permitted for age field!')
                    val = False

        if coln == 'DOB':
            if len(newval) != 10:
                mb.showerror('Invalid','Enter date in format YYYY-MM-DD!')
                val = False
            else:  
                bool = date(newval)
                if bool == False:
                    mb.showerror('Invalid','Enter a valid date!')
                    val = False
                
        else:  
            bool = date(newval)
            if bool == False:
                mb.showerror('Invalid','Enter a valid date!')
                val = False
        
                    
        if coln == 'Address':
            for i in newval:
                if i != ' ':
                    if i.isalpha() == False:
                        mb.showerror('Invalid','Only alphabets permitted for address field!')
                        val = False
                        break                            
                        
        if coln == 'Salary':
            if newval.isdigit() == False:
                mb.showerror('Invalid','Only integers permitted for salary field!')
                val = False
              
        if val == True:
            v = (newval,x)
            
            if coln == 'Name':
                q = "update Personal set Name = %s where User_ID = %s"
                cur.execute(q,v)
                con.commit()
                mb.showinfo('','Name succesfully modified!')
                            
            if coln == 'Age':
                q = "update Personal set Age = %s where User_ID = %s"
                cur.execute(q,v)
                con.commit()
                mb.showinfo('','Age succesfully modified!')
                    
            if coln == 'DOB':
                q = "update Personal set DOB = %s where User_ID = %s"
                cur.execute(q,v)
                con.commit()
                mb.showinfo('','DOB succesfully modified!')
                        
            if coln == 'Address':
                q = "update Personal set Address = %s where User_ID = %s"
                cur.execute(q,v)
                con.commit()
                mb.showinfo('','Address succesfully modified!')
                
            if coln == 'Salary':
                q = "update Personal set Salary = %s where User_ID = %s"
                cur.execute(q,v)
                con.commit()
                mb.showinfo('','Salary succesfully modified!')
#---------------------------------------------------------------------------------

#function to withdraw amount 
def wd(menu):
    f4=Frame(menu,width=685,height=400,bg='black')
    f4.place(x=400,y=115)

    l = Label(f4,text='Withdrawal ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',18,'bold'))
    l.place(x=270 ,y=30)
    Frame(f4,width=300,height=1,bg='white').place(x=195,y=70)
    
    l1 = Label(f4,text='Enter your Account number: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
    l1.place(x=233 ,y=90)
    e = Entry(f4,width=20,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
    e.place(x=250,y=120 )
    
    l2 = Label(f4,text='Enter amount of money to withdraw: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
    l2.place(x=205,y=160)
    e2 = Entry(f4,width=20,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
    e2.place(x=250,y=190)
    
    b = Button(f4,padx=10,width=16,text='Withdraw',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: wd_amt(e2.get(),e.get()))
    b.place(x=250,y=235)
    changeOnHover(b, "gainsboro","white")
    
    b2 = Button(f4,width=20, text='show balance',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10,'bold'),command=lambda: show_bal(f4,e.get()))
    b2.place(x=250,y=280)
    changeOnHover(b2, "gainsboro","white")
    
    back_btn = Button(f4,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f4))
    back_btn.place(x=310,y=320)
    changeOnHover(back_btn, "gainsboro","white")
    
#function to withdraw amount 
def wd_amt(amt,x):
    val = True
    bool = find_acct(x)
    
    if amt=='' or x=='':
        mb.showerror('Empty fields','Please fill all details!')
        val = False

    else:
        if amt.isdigit() == False:
                mb.showerror('Invalid','Only integers permitted for amount field!')
                val = False
        else:
            if bool == False:
                mb.showerror('Not found','The entered account number doesnt exist!')
                val = False
            else:
                bal_amt = get_bal_amt(x)
                if int(amt) >= int(bal_amt):
                    mb.showerror('No balance','Your account has only  Rs.'+bal_amt+'. Can not withdraw '+amt+'!')
                    val = False
                    
            if val == True:
                v=(amt,x)
                q= "update Account set deposit = deposit - %s where Acc_num = %s"
                cur.execute(q,v)
                con.commit()
                mb.showinfo('','Amount withdrawed successfully.')
#---------------------------------------------------------------------------------
            
#function to deposit amount                                                                                                                        
def dp(menu):
    f5=Frame(menu,width=685,height=400,bg='black')
    f5.place(x=400,y=115)

    l = Label(f5,text='Depositing',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',18,'bold'))
    l.place(x=270,y=30)
    Frame(f5,width=300,height=1,bg='white').place(x=195,y=70)
    
    l1 = Label(f5,text='Enter your Account number: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
    l1.place(x=233,y=90)
    e = Entry(f5,width=20,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
    e.place(x=250,y=120)
    
    l2 = Label(f5,text='Amount of money to deposit: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
    l2.place(x=230,y=160)
    e2 = Entry(f5,width=20,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
    e2.place(x=250,y=190)
    
    b = Button(f5,padx=10,width=16,text='Deposit',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: dp_amt(e2.get(),e.get()))
    b.place(x=250,y=235)
    changeOnHover(b, "gainsboro","white")
    
    b2 = Button(f5,width=20,text='show balance',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10,'bold'),command=lambda: show_bal(f5,e.get()))
    b2.place(x=250,y=280)
    changeOnHover(b2, "gainsboro","white")
    
    back_btn = Button(f5,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f5))
    back_btn.place(x=310,y=320)
    changeOnHover(back_btn, "gainsboro","white")
                            
#function to deposit amount                     
def dp_amt(amt,x):
    val = True
    bool = find_acct(x)
    
    if amt=='' or x=='':
        mb.showerror('Empty fields','Please fill all details!')
        val = False
    else:
        if amt.isdigit() == False:
                mb.showerror('Invalid','Only integers permitted for amount field!')
                val = False
        else:
            if bool == False:
                mb.showerror('Not found','The entered account number doesnt exist!')
                val = False
                    
            if val == True:
                v=(amt,x)
            q= "update Account set deposit = deposit + %s where Acc_num = %s"
            cur.execute(q,v)
            con.commit()
            mb.showinfo('','Amount deposited successfully.')
#---------------------------------------------------------------------------------

#function to delete details
def del_act(menu):
    f6=Frame(menu,width=685,height=400,bg='black')
    f6.place(x=400,y=115)

    #function to delete profile 
    def  nxt3():
        f6a = Frame(f6,width=685,height=400,bg='black')
        f6a.place(x=0,y=80)
        
        l = Label(f6a,text='Enter your User-ID: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
        l.place(x=280,y=30)
        e = Entry(f6a,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
        e.place(x=260,y=60)
        
        b = Button(f6a,padx=10,text='Delete',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12),command=lambda: del_user(e.get()))
        b.place(x=310,y=120)
        changeOnHover(b, "gainsboro","white")
        
        back_btn = Button(f6a,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f6a))
        back_btn.place(x=315,y=170)
        changeOnHover(back_btn, "gainsboro","white")

    #function to delete account
    def  nxt4():
        f6a = Frame(f6,width=685,height=400,bg='black')
        f6a.place(x=0,y=80)
        
        l = Label(f6a,text='Enter your account number: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
        l.place(x=245,y=30)
        e = Entry(f6a,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
        e.place(x=260,y=60)
        
        b = Button(f6a,padx=10,text='Delete',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12),command=lambda: del_acct(e.get()))
        b.place(x=310,y=120)
        changeOnHover(b, "gainsboro","white")
        
        back_btn = Button(f6a,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f6a))
        back_btn.place(x=315,y=170)
        changeOnHover(back_btn, "gainsboro","white")
                       
    h = Label(f6,text='Deleting Account',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',18,'bold'))
    h.place(x=250, y=30)
    Frame(f6,width=300,height=1,bg='white').place(x=195,y=70)
    
    l = Label(f6,text='Select what you want to delete: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',10))
    l.place(x=250,y=100)
    
    b1 = Button(f6,width=15,padx=10,pady=5,text='All my accounts',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: nxt3())
    b1.place(x=260,y=140)
    changeOnHover(b1, "gainsboro","white")
    
    b2 = Button(f6,width=15,padx=10,pady=5,text='One account',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: nxt4())
    b2.place(x=260,y=200)
    changeOnHover(b2, "gainsboro","white")
    
    back_btn = Button(f6,width=8,text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f6))
    back_btn.place(x=310,y=280)
    changeOnHover(back_btn, "gainsboro","white")
    
#function to delete a user from Personal table based on User_ID            
def del_user(x):
    val = True
    if x=='':
            mb.showerror('Empty fields','Please fill all details!')
            val = False
    else:
        bool = find_user(x)
        if bool == False:
            mb.showerror('Not found','The entered User-ID doesnt exist!')
            val = False
        if val == True:
            v = (x,)
            q1 = "delete from Personal where User_ID=%s"
            q2 = "delete from Account where User_ID=%s"
            cur.execute(q1,v)
            cur.execute(q2,v)
            con.commit()
            mb.showinfo('','User details deleted succesfully')

#function to delete an account from Account table based on Acc_Num
def del_acct(x):
    val = True
    if x=='':
            mb.showerror('Empty fields','Please fill all details!')
            val = False
    else:
        bool = find_acct(x)
        if bool == False:
            mb.showerror('Not found','The entered account number doesnt exist!')
            val = False
        if val == True:
            v = (x,)
            q = "delete from Account where Acc_Num=%s"
            cur.execute(q,v)
            con.commit()
            mb.showinfo('','Account details deleted succesfully')
#---------------------------------------------------------------------------------
            
#function to view balance
def bal(menu):
        f7=Frame(menu,width=685,height=400,bg='black')
        f7.place(x=400,y=115)

        h = Label(f7,text='Balance Enquiry',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',18,'bold'))
        h.place(x=260, y=50)
        Frame(f7,width=300,height=1,bg='white').place(x=195,y=90)
        
        l = Label(f7,text='Check the balance in your account here... ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',10))
        l.place(x=220,y=100)
        
        l1 = Label(f7,text='Enter your Acc_Num: ',fg='#57a1f8',bg='black',font=('Microsoft YaHei UI Light',12))
        l1.place(x=270,y=155)
        e1 = Entry(f7,width=20,fg='white',bg='black',font=('Microsoft YaHei UI Light',12))
        e1.place(x=260,y=190)
        
        b1 = Button(f7,padx=10,width=14,text='Show Balance',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: show_bal(f7,e1.get()))
        b1.place(x=270,y=240)
        changeOnHover(b1, "gainsboro","white")
        
        back_btn = Button(f7,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f7))
        back_btn.place(x=320,y=290)
        changeOnHover(back_btn, "gainsboro","white")

#function to view balance amount of an account      
def show_bal(menu,x):
    val = True
    if x=='':
            mb.showerror('Empty fields','Please fill all details!')
            val = False
    else:
        bool = find_acct(x)
        if bool == False:
            mb.showerror('Not found','The entered account number doesnt exist!')
            val = False
        if val == True:
            v = (x,)
            q = "select Acc_Num,deposit from Account where Acc_num=%s"
            cur.execute(q,v)
            res = cur.fetchall()
            
            f = Frame(menu,width=685,height=400,bg='black')
            f.place(x=0,y=0)
            back_btn=Button(f,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: back(f))
            back_btn.place(x=300,y=300)

            treef = Frame(f,width=685,height=300,bg='black')
            treef.place(x=0,y=0)
            tree = ttk.Treeview(treef)
            tree.pack(expand=True,fill=BOTH)

            tree['columns']=('Acc_Num','deposit')
            tree.column('#0',width=0,stretch=NO)
            tree.column('Acc_Num',anchor=W,width=100)
            tree.column('deposit',anchor=W,width=583)

            tree.heading('#0',text='')
            tree.heading('Acc_Num',text='Account No.',anchor=W)
            tree.heading('deposit',text='Balance',anchor=W)

            for i in range(len(res)):
                tree.insert(parent='',index='end', iid=i,text='',values=(res[i][0],res[i][1]))
                tree.pack(expand=True,fill=BOTH)
#---------------------------------------------------------------------------------
                
#function to create a submenu within menu window
def submenu(menu):
    global un
    username = un.get()
    smenu = Frame(menu,width=1180,height=600,bg='white')
    smenu.place(x=0,y=0)
    black_frame = Frame(menu,width=685,height=400,bg='black')
    black_frame.place(x=400,y=115)

    h1 = Label(smenu,padx = 100,text='Hello '+username+'!',fg='#3D59AB',bg='white',font=('Lucida Calligraphy',24,))
    h2 = Label(smenu,padx = 100,text=' ~ What would you like to do? ~ ',fg='#8470FF',bg='white',font=('Lucida Calligraphy',18))
    h1.place(x=500,y=10)
    h2.place(x=410,y=55)

    b1=Button(smenu,width=30,text='New Account',fg='white',bg='#3D59AB',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(smenu),submenu(menu),new_act(menu)])
    b1.place(x=50,y=120)
    changeOnHover(b1, "#8470FF", "#3D59AB")

    b2=Button(smenu,width=30,text='View Account',fg='white',bg='#3D59AB',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(smenu),submenu(menu),vw_acct(menu)])
    b2.place(x=50,y=170)
    changeOnHover(b2, "#8470FF", "#3D59AB")

    b3=Button(smenu,width=30,text='Modify Account',fg='white',bg='#3D59AB',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(smenu),submenu(menu),mod_act(menu)])
    b3.place(x=50,y=220)
    changeOnHover(b3, "#8470FF", "#3D59AB")
    
    b4=Button(smenu,width=30,text='Withdrawal',fg='white',bg='#3D59AB',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(smenu),submenu(menu),wd(menu)])
    b4.place(x=50,y=270)
    changeOnHover(b4, "#8470FF", "#3D59AB")

    b5=Button(smenu,width=30,text='Depositing',fg='white',bg='#3D59AB',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(smenu),submenu(menu),dp(menu)])
    b5.place(x=50,y=320)
    changeOnHover(b5, "#8470FF", "#3D59AB")

    b6=Button(smenu,width=30,text='Deleting Account',fg='white',bg='#3D59AB',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(smenu),submenu(menu),del_act(menu)])
    b6.place(x=50,y=370)
    changeOnHover(b6, "#8470FF", "#3D59AB")

    b7=Button(smenu,width=30,text='Balance Enquiry',fg='white',bg='#3D59AB',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(smenu),submenu(menu),bal(menu)])
    b7.place(x=50,y=420)
    changeOnHover(b7, "#8470FF", "#3D59AB")

    b8 = Button(smenu,width=30,text='Logout',fg= 'white',bg='#3D59AB',font=('Microsoft YaHei UI Light',12,'bold'),command=lambda: [back(smenu),submenu(menu),back(menu)])
    b8.place(x=50,y=470)
    changeOnHover(b8, "#8470FF", "#3D59AB")
#---------------------------------------------------------------------------------

#function to log in and create tables Personal and Account       
def login(username,password):
    if username !='' and password == '123':
        root.withdraw()
        global con, cur
        con=mc.connect(host='localhost',user='root',password='raybaehey7',db='sam')
        if con.is_connected():
                mb.showinfo("Login successful","Logged in")
                menu=Toplevel()
                menu.title('Bank Management Menu')
                menu.geometry('1180x600+300+200')
                menu.resizable(False,False)
                menu.configure(bg='#fff')
                cur=con.cursor()
                q="create table if not exists Personal (User_ID varchar(5) primary key, Name varchar(30), Age int(2), DOB date, Address varchar(30), Salary int(8))"
                cur.execute(q)
                q1="create table if not exists Account (Acc_Num varchar(5) primary key, Open_date date, deposit int(8), Acc_Desc varchar(20),User_ID varchar(5) references Personal(User_ID) on delete cascade on update cascade)"
                cur.execute(q1)
                submenu(menu)
                menu.mainloop()

    #credential validations 
    if password != '123':
        mb.showerror("Invalid","Invalid password!")
    if username == '':
        mb.showerror("Empty field","Please enter your username!")
#---------------------------------------------------------------------------------
        
#function to incorporate csv files 
def about(root):
    abt_pg = Toplevel(root)
    abt_pg.title('About')
    abt_pg.geometry('925x500+300+200')
    abt_pg.configure(bg='#fff')
    abt_pg.resizable(False,False)

    #Text file abt Capitol Bank- and CSV abt project?
    label = Label(abt_pg,fg ='#3D59AB',bg='white',text="ABOUT OUR PROJECT",font=('Microsoft YaHei UI Light',18,'bold'))
    label.place(x=352,y=10)

    Frame(abt_pg,width=300,height=1,bg='black').place(x=330,y=50)

    treef = Frame(abt_pg,width=750,height=300,bg='gainsboro')
    treef.place(x=80,y=100)
    
    back_btn = Button(abt_pg,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: close(abt_pg))
    back_btn.place(x=440,y=440)
    changeOnHover(back_btn, "gainsboro","white")

    tree = ttk.Treeview(treef)
    tree.place(x=0,y=0)
    tree.pack(expand=True,fill=BOTH)

    tree['columns']=('FUNCTIONS','PURPOSE')
    tree.column('#0',width=0,stretch=NO)
    tree.column('FUNCTIONS',anchor=W,width=150)
    tree.column('PURPOSE',anchor=W,width=620)
    #tree.column('FUNCTIONS USED',anchor=W,width=130)
    
    tree.heading('#0',text='')
    tree.heading('FUNCTIONS',text='FUNCTIONS',anchor=W)
    tree.heading('PURPOSE',text='PURPOSE',anchor=W)
    #tree.heading('FUNCTIONS USED',text='FUNCTIONS USED',anchor=W)
    
    f = open("abt.csv")
    robj = csv.reader(f)
    next(robj)
    for i in robj:
        tree.insert(parent='',index='end', iid=i,text='',values=(i[0],i[1]))
    tree.pack(expand=True,fill=BOTH)
    label = Label(abt_pg,fg ='#3D59AB',bg='white',text="ABOUT OUR PROJECT",font=('Microsoft YaHei UI Light',18,'bold'))
    label.place(x=352,y=10)

    Frame(abt_pg,width=300,height=1,bg='black').place(x=330,y=50)

    treef = Frame(abt_pg,width=750,height=300,bg='gainsboro')
    treef.place(x=80,y=100)
    
    back_btn = Button(abt_pg,width=8, text='Back',fg ='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',10),command=lambda: close(abt_pg))
    back_btn.place(x=440,y=440)
    changeOnHover(back_btn, "gainsboro","white")

    tree = ttk.Treeview(treef)
    tree.place(x=0,y=0)
    tree.pack(expand=True,fill=BOTH)

    tree['columns']=('FUNCTIONS','PURPOSE')
    tree.column('#0',width=0,stretch=NO)
    tree.column('FUNCTIONS',anchor=W,width=150)
    tree.column('PURPOSE',anchor=W,width=620)
    #tree.column('FUNCTIONS USED',anchor=W,width=130)
    
    tree.heading('#0',text='')
    tree.heading('FUNCTIONS',text='FUNCTIONS',anchor=W)
    tree.heading('PURPOSE',text='PURPOSE',anchor=W)
    #tree.heading('FUNCTIONS USED',text='FUNCTIONS USED',anchor=W)
    
    f = open("abt.csv")
    robj = csv.reader(f)
    next(robj)
    for i in robj:
        tree.insert(parent='',index='end', iid=i,text='',values=(i[0],i[1]))
    tree.pack(expand=True,fill=BOTH)
#---------------------------------------------------------------------------------
    
root = Tk()
root.title('Login - Capitol Bank')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)       
img = PhotoImage(file=r"bankpic.png")
Label(root,image=img).place(x=20,y=70)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=525,y=50)

welcome = Label(frame,text='Welcome to Capitol Bank!',fg='black',bg='white',font=('Microsoft YaHei UI Light',16,'italic')) 
welcome.place(x=55,y=2)

heading = Label(frame,text='~ LOGIN ~',fg='#3D59AB',bg='white',font=('Microsoft YaHei UI Light',28,'bold'))
heading.place(x=80, y=42)

unlabel = Label(frame,text='Username',fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
un = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
unlabel.place(x=30,y=120)
un.place(x=33,y=150)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=170)

pwlabel = Label(frame,text='Password',fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
pw = Entry(frame,width=35,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11),show='*')
pwlabel.place(x=30,y=195)
pw.place(x=33,y=220)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=240)

login_btn = Button(frame,width=32,padx=2,text='Login',fg='white',bg='#3D59AB',border=0,font=('Microsoft YaHei UI Light',12),command=lambda: login(un.get(),pw.get()))
login_btn.place(x=24,y=270)
changeOnHover(login_btn, "#8470FF", "#3D59AB")

abt_btn = Button(frame,width=32,padx=2,text='About',fg='white',bg='#3D59AB',border=0,font=('Microsoft YaHei UI Light',12),command=lambda: about(root))
abt_btn.place(x=24,y=320)
changeOnHover(abt_btn, "#8470FF", "#3D59AB")

root.mainloop()
